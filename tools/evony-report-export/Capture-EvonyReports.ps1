<#
.SYNOPSIS
  Saves lossless, full-resolution PNG screenshots of Evony battle reports from a MuMu emulator, using ADB.

.DESCRIPTION
  Screenshots only. The script reads what the emulator is showing and sends no taps, swipes or
  keystrokes to the game. You open and scroll each report yourself, then press Enter in this
  window to save the screen.

  For each report, capture: the main screen, the buffs screen, and the details screen (plus one
  extra capture per scroll if the details list is longer than one screen; let the captures overlap
  by a row or two).

.PARAMETER Instance
  MuMu instance number (0, 1, 2 ...). Used to work out the ADB port: 16384 + 32 * Instance.

.PARAMETER Port
  ADB port to use instead of -Instance (for example 16448).

.PARAMETER AdbPath
  Full path to adb.exe if it is not found automatically.

.PARAMETER OutDir
  Folder to save into. Defaults to a new evony-reports-<date-time> folder in the current folder.

.EXAMPLE
  .\Capture-EvonyReports.ps1
  .\Capture-EvonyReports.ps1 -Instance 2
  .\Capture-EvonyReports.ps1 -Port 16448 -OutDir D:\EvonyReports
#>
[CmdletBinding()]
param(
    [int]$Instance = 0,
    [int]$Port = 0,
    [string]$AdbPath = '',
    [string]$OutDir = ''
)

if ($Port -eq 0) { $Port = 16384 + 32 * $Instance }
$Serial = "127.0.0.1:$Port"
$RemoteFile = '/data/local/tmp/evony_report_cap.png'

function Find-Adb {
    if ($AdbPath) {
        if (Test-Path -LiteralPath $AdbPath) { return (Resolve-Path -LiteralPath $AdbPath).Path }
        throw "adb.exe not found at '$AdbPath'."
    }
    $onPath = Get-Command adb.exe -ErrorAction SilentlyContinue
    if ($onPath) { return $onPath.Source }

    $roots = @()
    foreach ($base in @($env:ProgramFiles, ${env:ProgramFiles(x86)}, 'C:\', 'D:\', 'D:\Program Files')) {
        if ($base) { $roots += (Join-Path $base 'Netease') }
    }
    foreach ($root in $roots) {
        if (Test-Path -LiteralPath $root) {
            $hit = Get-ChildItem -LiteralPath $root -Recurse -Filter adb.exe -ErrorAction SilentlyContinue |
                Select-Object -First 1
            if ($hit) { return $hit.FullName }
        }
    }
    throw "adb.exe not found. Re-run with -AdbPath 'C:\path\to\adb.exe'. MuMu ships one inside its install folder."
}

function Get-PngSize([string]$Path) {
    $bytes = New-Object byte[] 24
    $fs = [System.IO.File]::OpenRead($Path)
    try { [void]$fs.Read($bytes, 0, 24) } finally { $fs.Dispose() }
    $isPng = ($bytes[0] -eq 0x89) -and ($bytes[1] -eq 0x50) -and ($bytes[2] -eq 0x4E) -and ($bytes[3] -eq 0x47)
    if (-not $isPng) { return $null }
    $w = [int]$bytes[16] * 16777216 + [int]$bytes[17] * 65536 + [int]$bytes[18] * 256 + [int]$bytes[19]
    $h = [int]$bytes[20] * 16777216 + [int]$bytes[21] * 65536 + [int]$bytes[22] * 256 + [int]$bytes[23]
    return "${w}x${h}"
}

$adb = Find-Adb
Write-Host "Using adb: $adb"

& $adb connect $Serial | Out-Null
$state = (& $adb -s $Serial get-state | Out-String).Trim()
if ($state -ne 'device') {
    throw "Cannot reach the emulator at $Serial (state: '$state'). Start that MuMu instance, check its ADB port, then try again."
}

if (-not $OutDir) {
    $OutDir = Join-Path (Get-Location) ('evony-reports-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
}
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$OutDir = (Resolve-Path -LiteralPath $OutDir).Path
Write-Host "Saving to:  $OutDir"
Write-Host ''
Write-Host 'Open a report in the game, then use this window:'
Write-Host '  [Enter]  save the current screen'
Write-Host '  n        start the next report'
Write-Host '  u        delete the last capture (retake it)'
Write-Host '  q        quit'
Write-Host ''

$report = 1
$part = 1
$last = $null

:capture while ($true) {
    $key = (Read-Host ("Report {0:D3}, part {1:D2}" -f $report, $part)).Trim().ToLower()
    switch ($key) {
        'q' { break capture }
        'n' {
            if ($part -gt 1) { $report++ ; $part = 1 ; $last = $null }
            Write-Host "Now on report $('{0:D3}' -f $report)."
            continue capture
        }
        'u' {
            if ($last -and (Test-Path -LiteralPath $last)) {
                Remove-Item -LiteralPath $last
                Write-Host "Deleted $(Split-Path $last -Leaf)."
                $part--
                $last = $null
            } else {
                Write-Host 'Nothing to delete.'
            }
            continue capture
        }
        '' {
            $name = 'report-{0:D3}_part-{1:D2}.png' -f $report, $part
            $file = Join-Path $OutDir $name
            & $adb -s $Serial shell screencap -p $RemoteFile | Out-Null
            & $adb -s $Serial pull $RemoteFile $file | Out-Null
            & $adb -s $Serial shell rm -f $RemoteFile | Out-Null
            $size = $null
            if (Test-Path -LiteralPath $file) { $size = Get-PngSize $file }
            if ($size) {
                Write-Host "  saved $name ($size)"
                $last = $file
                $part++
            } else {
                Write-Host '  capture failed; check the emulator is running and try again.'
            }
            continue capture
        }
        default { Write-Host 'Use Enter, n, u or q.' }
    }
}

Write-Host "Done. Screenshots are in $OutDir"
