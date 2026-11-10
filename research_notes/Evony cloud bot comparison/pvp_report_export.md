# Exporting, Capturing and Sharing PvP Battle Reports in Evony: The King's Return (TKR)

Research date: 2026-11-10. Method note: in this cloud session, WebFetch could not reach any outside host (evonyguidewiki.com, tactica-ai.com, getsharex.com, evonytools.it.com, top.gg and evonyplayersguide.blogspot.com all failed DNS resolution), and reddit.com was blocked for search. So every finding below comes from search-engine result summaries and snippets, not full-page reads. Treat specifics as "verify on the live page". To check them, allow those hosts in the session's network settings and fetch the pages again.

## Q1. In-game options: share button, report link/ID, web viewer, what a shared report keeps, and how long reports last

### Takeaway
I found no current (2024–2026) source that documents TKR's in-game "share report" flow, report links or IDs, a web viewer, or mailbox limits. What I did find: TKR mail has a star/favorite (a "Saved" mailbox) that protects reports from frequent automatic deletion. A full PvP report spans at least three screens (main, buffs, details). Several community sources say the report does not show every buff. Every "temporary report URL" or "evonyurl" sharing method I found belongs to the original 2009-era browser Evony (historical), not TKR.

### Cited Findings
- **Favorites/Saved mail (TKR):** You save a mail by tapping the star icon at the bottom of it, and the guide warns that "mail gets deleted frequently, so if there is something you really want to keep around, make sure to use that star icon." The page is dated 2019-11-26, so menu positions may have changed. — [Evony TKR Player's Guide: 4. Mail, Chat, and Whisper](https://evonyplayersguide.blogspot.com/p/beginner-tip-4-mail-chat-and-whisper.html)
- **Same guide:** a "T" icon on each mail translates it. Chat has three channels (World, Alliance, Whisper), and you switch between them by swiping the text box above the main screen. Alliance Chat opens when you tap the text box at the bottom of the main screen. — [Evony TKR Player's Guide: 4](https://evonyplayersguide.blogspot.com/p/beginner-tip-4-mail-chat-and-whisper.html)
- **Alliance mail permissions (TKR):** R4s and R5 "can also send alliance mail", which implies ordinary members may not be able to mass-mail a report to the alliance. — [Evony TKR Player's Guide: 5. Alliances](https://evonyplayersguide.blogspot.com/p/beginner-tip-5-alliances.html)
- **A "Saved mailbox" exists for favorited reports:** Tactica's "Fast Read" imports "favorited reports" from the "Saved mailbox" without opening each one in game (vendor claim, current site). — [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html); [Tactica FAQ](https://www.tactica-ai.com/faq.html)
- **Report structure:** a TKR battle report has at least a **main** view, a **buffs** view and a **details** view. Tactica's reader "opens the report, taps and scrolls through the main screen, the buffs screen, and the details screen". — [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html)
- **Data fields a report contains (per Tactica's stored record):** troop layers with type, tier, survived, killed, wounded, deserter, "holy palace" and killing counts, plus generals, buffs/debuffs and timestamps. The search results did not mention equipment as a stored field. — [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html)
- **Buffs are only partly visible in reports:** the community wiki says buffs are "generally not shown in the battle report". Marching and reinforcement buffs can be toggled to see how wounded counts change, and the report shows the rally owner's buffs. Hidden buffs still apply in combat. The buff value shown changes depending on whether a subordinate city is linked and on certain Monarch talents. — [Evony Guide Wiki: Buff/Debuff basic guide](https://evonyguidewiki.com/en/buff_debuff_basic_guide-en/)
- **Partly conflicting wiki statement:** "PvP battle reports show player buff percentages", but monster-specific buffs are not included. — [Evony Guide Wiki: How Many Troops need to Defeat Boss?](https://evonyguidewiki.com/en/how-many-troops-defeat-boss-en/). This contrasts with the "generally not shown" wording above. The likely reading is that the report shows *aggregate* attack/defense/HP percentages but not the per-source buff breakdown. That reading is my inference and is unverified.
- **Specific buff visibility tests:** Blazon set buffs appear in the report's debuff column. A Duty Officer specialty buff (Minamoto no Yoshitsune's Ranged Troop Assault) did not change report values when tested. — [Evony Guide Wiki: Blazon](https://evonyguidewiki.com/en/blazon-en/); [Evony Guide Wiki: Duty Officer Guide](https://evonyguidewiki.com/en/duty-officer-guide-en/)
- **HISTORICAL (original browser Evony, not TKR):** each attack report had a "url" at the bottom that was "a temporary cache of your attack report", which players pasted into alliance chat or mail. Attacks on other players showed automatically under Alliance > "war report". — [Answers.com Q&A](https://www.answers.com/Q/How_do_you_upload_battle_reports_on_Evony_so_your_alliance_can_see_them) (undated; describes the old browser game)
- **HISTORICAL:** the 2010 official forum describes alliance-wide mail sent from the Alliance > members tab, costing "speakers". — [bbs.evony.com: Alliance Mail (2010)](http://bbs.evony.com/showthread.php?163129-Alliance-Mail)
- **UNVERIFIED / possibly a different game:** a 2015 blog post describes an icon on the lower left of a detailed report for sending it to alliance members, where a green checkmark selects every alliance member. The excerpt does not name the game, and it predates TKR's 2016 launch. — [Threatmasters: Sending and Reading Battle Reports (2015-02-06)](https://threatmasters.wordpress.com/2015/02/06/sending-battle-reports/)
- **A different game, not to be confused with TKR:** March of Empires has an Army > Reports > "Share" icon. — [Gameloft Help Center (March of Empires)](https://gameloft.helpshift.com/hc/en/22-march-of-empires/faq/1667-can-i-share-scout-and-battle-reports-with-alliance-members/?p=all)

### Inferences
- Because "mail gets deleted frequently", players should **star a report right after the battle** before capturing or sharing it. Any later export method (screenshots, Tactica Fast Read) depends on the report still being in the Saved mailbox.
- Even a perfect in-game share cannot give a full per-source buff breakdown, because the report itself does not show all buffs (wiki). Any export method is therefore capped at the precision of the report's main, buffs and details screens.
- No source showed a TKR web viewer or a public report URL or ID. If one existed, a third-party tool like Tactica would likely use it instead of driving an emulator. Tactica's emulator-driven design is indirect evidence that no web or API export exists (inference).

### Gaps
- **TKR's current in-game "Share" flow is unconfirmed by any source found.** I could not confirm whether reports can be shared to alliance or world chat or forwarded by mail, whether a shared report is clickable and opens the full report (including buffs and details tabs) for the recipient, or whether it drops data. Someone needs to check this in game.
- Mailbox capacity, retention period (days), and the cap on starred/Saved reports: no source found.
- Whether shared-in-chat reports expire: unknown.
- Whether equipment and general skill details appear in reports: not confirmed by sources (Tactica's field list does not mention equipment).

## Q2. Screenshot-based capture: high-resolution best practice, scrolling and long screenshots, stitching, crisp text

### Takeaway
The cleanest free method is **native screenshots from a large-window PC client or Android emulator**, one per report screen (main, buffs, details), with the emulator's resolution and DPI raised. Built-in phone scroll capture (Android "Capture more", iOS full-page) generally does not work inside games. ShareX scrolling capture (free, open source) is the best free Windows option for the scrolling details list. It may still fail on game canvases and needs testing.

### Cited Findings
- **PC clients exist:** TKR is listed on the Microsoft Store for Windows (the listing notes chat and real-time voice translation) and on Google Play Games for PC. — [Microsoft Store listing](https://apps.microsoft.com/detail/9p2rh449lvl2?hl=en-US); [Google Play Games PC listing](https://play.google.com/pc-store/games/details?id=com.topgamesinc.evony)
- **BlueStacks 5 display settings:** resolution, DPI and orientation are under Settings > Display. Presets are 160/240/320 DPI, and a custom value of 1–999 is allowed (requires restart). — [BlueStacks Support: Custom DPI (JA)](https://support.bluestacks.com/hc/articles/4406352472461)
- **DPI is not pixels:** DPI changes the density and apparent size of the Android UI. It does not add physical pixels. (Third-party page, moderate reliability.) — [macmyths: best display settings for BlueStacks 5](https://macmyths.com/what-are-the-best-display-settings-for-bluestacks-5/)
- **MuMu sizing on Windows:** if the window size is wrong, MuMu's official FAQ says to change the shortcut's Compatibility > DPI setting and uncheck the High DPI scaling override. — [MuMu FAQ: emulator inconsistent in size](https://www.mumuglobal.com/faq/emulator-inconsistent-in-size.html)
- **Tactica's import works only on emulators:** Fast Read requires MuMu ("does not work on BlueStacks"). Read/Bulk Read works on any ADB-compatible Android emulator. — [Tactica FAQ](https://www.tactica-ai.com/faq.html)
- **Android native scroll capture:** "Capture more" (Android 12+, Power + Volume Down) supports "most scrollable screens, not every screen". — [Laptop Mag: scrolling screenshots on iPhone and Android](https://www.laptopmag.com/how-to/take-scrolling-screenshots-on-iphone-and-android); [Gizmodo](https://gizmodo.com/how-to-take-scrolling-screenshots-on-any-device-1848335524)
- **Not for games:** scrolling capture "will not be activated for static content that does not scroll vertically, such as games or films". — [Mezha: long scrolling screenshot on Android and iOS](https://mezha.media/en/articles/how-to-take-a-long-scrolling-screenshot-on-android-and-ios)
- **iOS full-page capture** is documented for Safari web pages. Other apps support it only if they implement Apple's UIScreenshotService. — [Gadget Hacks: Safari iOS 13 full-page](https://ios.gadgethacks.com/how-to/take-scrolling-screenshots-entire-webpages-safari-ios-13-0198601/); [Tom's Guide: Capture more on iOS](https://tomsguide.com/hones/capture-more-how-to-take-a-scrolling-screenshot-on-ios-and-ipados)
- **Third-party Android stitchers:** before native support, LongShot and Stitchcraft were the main options. — [Laptop Mag](https://www.laptopmag.com/how-to/take-scrolling-screenshots-on-iphone-and-android)
- **ShareX (Windows) is free and open source.** Its scrolling capture has options to detect scroll end, remove duplicate images, guess offsets and combine images. — [ShareX docs: Scrolling screenshot](https://getsharex.com/docs/scrolling-screenshot); [listoffreeware](https://listoffreeware.com/?p=58627)
- ShareX scrolling capture "automatically stops if the first image combine attempt fails", and the hotkey toggles start and stop. — [ShareX changelog](https://GetShareX.com/changelog)
- **ShareX 17.0 (January 2025)** improved scrolling capture and added "Auto ignore bottom edge", which compares images to find static parts at the bottom in addition to the default 50 px. — [AlternativeTo news, Jan 2025](https://alternativeto.net/news/2025/1/sharex-17-0-released-with-enhanced-scrolling-capture-notification-sounds-and-much-more/); [Neowin: ShareX 17.0](https://www.neowin.net/news/sharex-170-is-out-with-improved-scrolling-capture-and-more/)

### Inferences
- **Best free practice (inferred):** run TKR on the Windows PC client or an emulator. Maximize the window or set a high emulator resolution (for example 1920x1080 or 2560x1440) with a moderate DPI, so more rows fit per screen and text renders larger. Take a lossless PNG of each of the main, buffs and details screens. Scroll the details screen and take overlapping shots. Fewer, larger screenshots reduce stitching errors.
- **ShareX on a game window:** ShareX scrolling capture works by sending scroll input and stitching frames. Whether TKR's details list responds to mouse-wheel scrolling in a way ShareX can stitch is untested. The changelog's auto-stop behavior suggests it will simply fail rather than produce a wrong image, so trying it costs little.
- **Phones:** because native scroll capture does not engage in games, mobile users should take several overlapping screenshots and either post them as an album or stitch them with a free stitching app. The mobile capture size is fixed by the device's native resolution, so phones with higher resolution give crisper text.
- **Keep text crisp:** save PNG rather than JPEG, avoid in-app image compression (some chat apps re-compress), and do not upscale.

### Gaps
- I found no TKR-specific capture guide (YouTube, Reddit or wiki) that recommends particular resolution or DPI values for reports.
- Untested: whether ShareX scrolling capture works on the TKR details screen in the PC client or an emulator.
- The emulators' built-in screenshot tools (BlueStacks/MuMu screenshot buttons, default save formats and resolutions) were not confirmed from official docs in this session.
- Stitching tool comparisons (for example free desktop stitchers) were not researched in depth.

## Q3. Text/data extraction: parsers, analyzers, Discord bots, third-party bots that export text, JSON or CSV

### Takeaway
The only current TKR-specific tool I found that turns reports into structured data is **Tactica** (tactica-ai.com). It is a paid Windows app that drives an Android emulator to read the main, buffs and details screens of each report into a library. It has **no CSV or JSON export**: you can only copy tables generated in its Analyst into a spreadsheet. Older "battle report calculators" such as dxcalc are for the original browser Evony (historical). Current Evony Discord bots focus on map intel, calculators and reminders, not report parsing.

### Cited Findings
- **Tactica: what it is.** A Windows desktop app that imports Evony battle reports into a searchable library and runs "Battlefield Analyst" over one battlefield at a time (for example, a hit-sequence timeline for a keep, with heals and movement between hits). All claims are the vendor's own. — [Tactica home](https://www.tactica-ai.com/); [How to Analyze Hundreds of Evony Battle Reports](https://www.tactica-ai.com/analyze-evony-battle-reports.html)
- **Tactica: how it captures.** "Fast Read" (MuMu only, Saved mailbox) pulls favorited reports without opening each in game. "Read / Bulk Read" works on any ADB-compatible emulator and taps and scrolls through each report's main, buffs and details screens. — [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html); [Tactica FAQ](https://www.tactica-ai.com/faq.html)
- **Tactica: fields stored.** Troop layers (type, tier, survived, killed, wounded, deserter, holy palace, killing), generals, buffs/debuffs, timestamps. — [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html)
- **Tactica: export.** "The on-disk format is proprietary. There is no CSV or JSON dump of the library." Tables generated in Battlefield Analyst have a copy button for pasting into a spreadsheet. — [Tactica FAQ](https://www.tactica-ai.com/faq.html)
- **Tactica: accuracy.** "Points given up are exact: fallen troops priced with the per-troop point table". Its "Effectiveness" metric is a cost-benefit measure that it says it never calls "exact points scored". — [Tactica: Effectiveness](https://www.tactica-ai.com/effectiveness.html)
- **Tactica: OCR inconsistency.** The download page lists "Advanced OCR battle report parsing", while other pages present Fast Read as avoiding OCR problems. No independent accuracy reviews were found. — [Tactica Download](https://www.tactica-ai.com/download.html)
- **Tactica: privacy etiquette.** "Do not send other players' screenshots or identifiable report dumps without consent." — [Tactica cookbook](https://www.tactica-ai.com/cookbook.html)
- **Evony Scanner** (evonytools.it.com) is a Discord bot that streams map intel into alliance channels: enemy keep activity, monster spawns, marches. It says it does not automate or play the game and is not affiliated with Top Games Inc. No battle report export is mentioned. — [Evony Scanner](https://evonytools.it.com/)
- **EvonyCompanion** (Discord bot on top.gg) offers guides, calculators and alliance tools. No report parsing is mentioned in the results. — [top.gg: EvonyCompanion](https://top.gg/bot/874070275824701470)
- **Evony Reminder Bot** offers JSON export, but only of events, weekly schedules and backups, not battle reports. — [top.gg: Evony Reminder Bot](https://top.gg/vi/bot/1434569785756090510)
- **HISTORICAL (browser Evony, not TKR):** dxcalc, "Dxter's Evony Battle Calculator", loads Evony battle and scout reports directly and accepts "evonyurl" reports. It also has an "Update defense" feature. Trap counts are server-random, with a typical trap rate of 4.0–9.0. — [dxcalc help](https://dxcalc.com/share/info.html)

### Inferences
- For **precise structured text** (per-troop-tier losses) at low cost, the realistic options are: (a) manual transcription from screenshots into a Google Sheet template (free, slow), (b) a generic OCR of crisp PNG screenshots followed by manual checking (free, error-prone on numbers, icons and troop tiers), or (c) Tactica ($14.99/mo) for automated capture but no raw export.
- Tactica reads screens through an emulator, so its accuracy is bounded by what the report displays, including the buff visibility limits in Q1 (inference).
- Tactica and any "bot" that automates the game client through ADB may carry Terms of Service risk with Top Games. See the separate risks/policy notes. I did not read TKR's ToS in this session.

### Gaps
- I found **no free OCR-based TKR report parser, Discord bot that reads report screenshots, GitHub repo or community spreadsheet** in the results. Reddit and GitHub could not be searched or fetched directly (Reddit is blocked to the search agent), so absence is not proof that none exists.
- Whether any cloud or local TKR automation bot (the subject of the parent comparison) exports battle reports as text, JSON or CSV: no source found.
- Tactica's actual OCR or reader accuracy and its error rate on large rallies: no independent data.
- Generic OCR accuracy on TKR report screenshots (Google Lens, Windows Snipping Tool text actions, Tesseract): not tested or sourced.

## Q4. Sharing with an alliance: Discord, image hosts, Google Sheets, community-standard formats

### Takeaway
No community-standard TKR report-posting format was found. The practical low-cost pattern is: star the report in game, share it in Alliance Chat if the client allows it (unconfirmed), and post lossless screenshots of the main, buffs and details screens to a dedicated Discord channel. Log key numbers in a shared Google Sheet if you want trends. Tactica offers a paid shared alliance library, with view-only seats at $2.49/month.

### Cited Findings
- **Player guide etiquette (TKR):** "If you scout an enemy, post the report in alliance chat". Questions that others may benefit from go in Alliance Chat, not Whisper. — [Evony TKR Player's Guide: 5. Alliances](https://evonyplayersguide.blogspot.com/p/beginner-tip-5-alliances.html); [Evony TKR Player's Guide: 4](https://evonyplayersguide.blogspot.com/p/beginner-tip-4-mail-chat-and-whisper.html)
- **Only R4 and R5 can send alliance mail.** — [Evony TKR Player's Guide: 5. Alliances](https://evonyplayersguide.blogspot.com/p/beginner-tip-5-alliances.html)
- **Tactica's shared library:** subscribing members can "join up in Tactica to share a library of reports and split who scans them in". View-only members need no emulator. — [Tactica FAQ](https://www.tactica-ai.com/faq.html)
- **Discord is the hub for existing Evony alliance tooling** (map-intel bots, calculators). — [Evony Scanner](https://evonytools.it.com/); [top.gg: EvonyCompanion](https://top.gg/bot/874070275824701470)
- **Consent norm:** do not share other players' screenshots or identifiable report dumps without consent. — [Tactica cookbook](https://www.tactica-ai.com/cookbook.html)

### Inferences
- **Suggested lightweight post format (inferred, not a community standard):** one Discord message per battle, with a header line (date/time UTC, server, attacker → target, type: attack/defense/rally/scout, outcome), followed by the PNG screenshots in order (main → buffs → details 1..n), plus a thread for discussion. Posting the files directly in Discord avoids a separate image host. Check whether Discord compresses images for your account tier before relying on it.
- A **Google Sheets template** (one row per report; columns for troop type, tier, sent, killed, wounded, survived, plus a screenshot link) mirrors the fields Tactica stores and gives structured data for free. It requires manual entry.

### Gaps
- Community-standard formats or templates for posting TKR PvP reports (Discord or Sheets): none found.
- Discord's current upload size and compression limits for free accounts were not researched in this session.

## Q5. Costs: free vs paid, subscriptions

### Takeaway
Everything except Tactica is free: in-game starring and chat, PC client and emulators, OS screenshots, ShareX, Discord and Google Sheets. Tactica is $14.99/month per full user after a 7-day trial, plus Analyst overage. Alliance view-only seats are $2.49/month, or $17.99/month for 10 seats.

### Cited Findings
- **Tactica pricing:** the full desktop app is $14.99/month after a 7-day free trial, and extra Battlefield Analyst use is billed as overage. Alliance view-only seats are $2.49/month. "Rally Squad" is 10 view-only seats for $17.99/month (about 28% less than 10 individual seats). Adding new reports requires a full subscription. — [Tactica FAQ](https://www.tactica-ai.com/faq.html); [Tactica Download](https://www.tactica-ai.com/download.html)
- **ShareX is free and open source.** — [ShareX docs](https://getsharex.com/docs/scrolling-screenshot); [Neowin: ShareX 17.0](https://www.neowin.net/software/sharex-170/)
- **The TKR PC clients are free to download** (Microsoft Store and Google Play Games on PC listings). — [Microsoft Store](https://apps.microsoft.com/detail/9p2rh449lvl2?hl=en-US); [Google Play Games PC](https://play.google.com/pc-store/games/details?id=com.topgamesinc.evony)
- **Free Evony Discord bots exist** (Evony Scanner, EvonyCompanion), but none parse reports. — [Evony Scanner](https://evonytools.it.com/); [top.gg: EvonyCompanion](https://top.gg/bot/874070275824701470)

### Inferences
- For a typical alliance, the lowest cost with good precision is $0: PC or emulator screenshots, a Discord channel and a shared Sheet. Paying for Tactica only makes sense when the alliance needs bulk analysis of hundreds of reports per battlefield (KvK, Battle of Gaugamela/Constantinople, and similar). One scanner at $14.99/month plus view-only seats is the cheapest paid setup.

### Gaps
- Exact Tactica overage rates: not captured in snippets.
- Emulator costs: BlueStacks and MuMu are generally free with ads or premium tiers, but this was not confirmed from official pricing pages in this session.

## Overall ranked comparison (objective synthesis)

### Takeaway
Ranked by precision-per-dollar for an alliance: (1) star in game, then capture lossless PNGs of each screen from the PC client or an emulator, then post to Discord; (2) the same plus manual entry into a Google Sheet for structured data; (3) ShareX scrolling capture for long details lists (free, needs testing); (4) phone screenshots, multiple and overlapping; (5) Tactica (paid; the only automated structured capture found, but no raw export); (6) in-game share or forward (free, data stays in game, but the TKR flow is unverified). Historical tools (dxcalc, evonyurl) do not apply to TKR.

### Cited Findings
| Rank | Method | Cost | Quality/precision | Effort | Limits | Key sources |
|---|---|---|---|---|---|---|
| 1 | Star report in game, then PNG screenshots of the main, buffs and details screens on the PC client or a high-resolution emulator, posted to a Discord channel | Free | Pixel-exact copy of everything the report shows. Limited by the report's own buff visibility | Low–medium (several shots per report) | Manual. Details list may need several overlapping shots | [Player's Guide 4](https://evonyplayersguide.blogspot.com/p/beginner-tip-4-mail-chat-and-whisper.html); [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html); [BlueStacks DPI](https://support.bluestacks.com/hc/articles/4406352472461); [Buff guide](https://evonyguidewiki.com/en/buff_debuff_basic_guide-en/) |
| 2 | Rank 1 plus manual transcription into a Google Sheet (fields: troop type/tier, killed, wounded, survived, generals, buffs) | Free | Structured. Accuracy depends on the person typing | High | Slow for big rallies | Field list from [Tactica: How it works](https://www.tactica-ai.com/how-it-works.html) |
| 3 | ShareX scrolling capture of the details screen (Windows) | Free, open source | One stitched image if it works. Auto-stops on failure | Low once configured | Untested on the TKR game canvas | [ShareX docs](https://getsharex.com/docs/scrolling-screenshot); [ShareX changelog](https://GetShareX.com/changelog); [AlternativeTo Jan 2025](https://alternativeto.net/news/2025/1/sharex-17-0-released-with-enhanced-scrolling-capture-notification-sounds-and-much-more/) |
| 4 | Phone screenshots, multiple and overlapping (native scroll capture will not engage in games) | Free | Fixed by device resolution | Medium | No long capture in games | [Mezha](https://mezha.media/en/articles/how-to-take-a-long-scrolling-screenshot-on-android-and-ios); [Laptop Mag](https://www.laptopmag.com/how-to/take-scrolling-screenshots-on-iphone-and-android) |
| 5 | Tactica (emulator-driven reader, shared alliance library, AI analyst) | $14.99/mo full user (7-day trial) + overage; $2.49/mo view-only; $17.99/mo for 10 view-only | Structured fields. Vendor claims exact loss points. No independent accuracy data | Low per report (bulk) | Windows plus emulator (Fast Read: MuMu only). Proprietary storage, **no CSV/JSON export**. Possible ToS risk | [Tactica FAQ](https://www.tactica-ai.com/faq.html); [How it works](https://www.tactica-ai.com/how-it-works.html); [Download](https://www.tactica-ai.com/download.html) |
| 6 | In-game share to Alliance Chat or forward by mail | Free | Full in-game fidelity for in-game viewers (unverified) | Very low | Flow unconfirmed for TKR. Alliance mail is R4/R5 only. Retention unknown. Not viewable outside the game | [Player's Guide 5](https://evonyplayersguide.blogspot.com/p/beginner-tip-5-alliances.html) |
| — | HISTORICAL: evonyurl / temporary report URL / dxcalc | Free | n/a for TKR | n/a | Original 2009-era browser Evony only | [dxcalc](https://dxcalc.com/share/info.html); [Answers.com](https://www.answers.com/Q/How_do_you_upload_battle_reports_on_Evony_so_your_alliance_can_see_them) |

### Inferences
- In-game share is ranked last for shareability, not quality. It cannot be archived or viewed outside the game, and its TKR behavior is unverified. If a working share-to-Alliance-Chat exists, alliances should use it as the instant first step alongside screenshots (Rank 1), not instead of them.
- No method exceeds the report's own precision. Full per-source buff breakdowns are not available from reports, according to the community wiki.

### Gaps
- An in-game check of TKR's report share and forward options, mailbox and Saved limits, and whether shared reports keep the buffs and details tabs.
- Independent user reviews of Tactica. Reddit, YouTube and GitHub searches were not possible in this session (Reddit is blocked to the search agent, and page fetching was blocked by network policy).
- Whether any free OCR or Discord report parser exists for TKR.
