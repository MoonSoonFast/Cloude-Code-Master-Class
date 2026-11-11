# Evony battle report export

A free workflow for getting PvP battle reports out of Evony: The King's Return as sharp images and a clean spreadsheet.

1. **Capture** each report as lossless PNGs, from the MuMu emulator (script below) or the Windows PC client (ShareX).
2. **Extract** the numbers into `report-template.csv` by sending the PNGs to Claude.
3. **Share** the PNGs in your alliance Discord and the CSV as a Google Sheet.

Nothing here taps, swipes or reads game memory. It only saves what is on screen.

## One login at a time

Evony allows one session per account. If an account is running in ESB Cloud, opening it on the emulator or PC client signs the cloud bot out until you leave, or signs you out. Capture reports while the bot is paused, or from an account that isn't botted.

## 1a. Capture from MuMu with `Capture-EvonyReports.ps1`

ADB `screencap` reads the emulator's own screen at its full resolution. The result has no window border, no compression and no blur, which is the best quality you can get without a dedicated tool.

1. **Set the resolution once.** In MuMu's settings, go to Display, pick a phone layout (1080×1920 or higher), and restart the instance. A higher resolution gives sharper text.
2. **Get the script.** Download `Capture-EvonyReports.ps1` from this folder.
3. **Run it** in PowerShell from the download folder:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\Capture-EvonyReports.ps1 -Instance 0
   ```

   `-Instance 1` and `-Instance 2` select your other MuMu instances. They use ports 16416 and 16448. You can also pass `-Port 16448` directly.
4. **Capture each report.** In the game, star the report so it isn't deleted, then open it. Press **Enter** in the PowerShell window for each screen: the main screen, buffs and details. If details are longer than one screen, scroll it yourself, keeping a row of overlap, and press Enter again.
5. **Use the keys.** Press **n** to start the next report, **u** to delete and retake the last capture, and **q** to quit.

Files are saved as `evony-reports-<date>\report-001_part-01.png`, `report-001_part-02.png` and so on.

If the script can't find `adb.exe`, add `-AdbPath "C:\path\to\MuMu\...\adb.exe"`. MuMu installs its own copy inside its program folder.

## 1b. Capture from the Windows PC client with ShareX

ShareX is free (getsharex.com).

1. Set the game window to full screen or as large as possible.
2. In ShareX, open **After capture tasks**, turn on **Save image to file**, and set the format to **PNG**.
3. Press **Alt + Print Screen** to capture the active window. Open the report, capture each screen, and scroll the details as in 1a.

ShareX's scrolling capture might stitch the details list into one image, but nobody has tested it with Evony. Overlapping screenshots always work.

## 2. Turn the screenshots into a spreadsheet

1. **Send them to Claude.** Upload one report's PNGs (all its parts) to Claude with: *"Transcribe this Evony battle report into the columns of report-template.csv, one row per troop line. Flag any number you can't read clearly instead of guessing."*
2. **Get the rows back.** You get CSV rows back. Claude checks that killed, wounded and survived add up to the starting troops wherever the report shows all of them, and flags any row that doesn't.
3. **Paste them in.** Paste the rows into a shared Google Sheet.

This costs nothing beyond your Claude plan, and reads the game's styled fonts more reliably than free OCR such as Tesseract.

**The report is the limit.** Evony reports don't show every buff source. No export can be more precise than what the game prints.

## Files

| File | What it is |
|---|---|
| `Capture-EvonyReports.ps1` | Screenshot-only ADB capture for MuMu |
| `report-template.csv` | Columns for the extracted data |
