# Evony: The King's Return (TKR) Bot Landscape, 2025–2026 (cloud-hosted vs local)

Research date: 2026-11-10.

**Method note (read first):** Direct page fetches failed for most vendor domains in this session: evonyauto.com, evonai.app, gnbots.com and fbots.org could not be resolved through the session's network policy. Reddit is also blocked to the search tool. Every vendor fact below therefore comes from search-engine summaries and snippets of those vendor pages, not from a direct read of the page. The URLs cited are the vendor pages the snippets came from. Prices and features are as the vendors advertise them, and several vendors contradict themselves across their own pages (flagged inline). Re-verify on the live checkout page before relying on any number.

## Q1. What bots exist for Evony TKR, cloud vs local, and how do they compare?

### Takeaway
I found 16 vendor bots or bot services marketed for Evony TKR in 2025–2026.
- **Browser-controlled cloud bots (no emulator on the user's side):** Evony Auto, EvonAI, GNBots Evony Cloud Bot, ESB Cloud, iScope Auto, and Fbots' server plans. The newest of these (Evony Auto, EvonAI, ESB Cloud) link to your game account with an email-verification code rather than a password.
- **Hybrids:** BoostBot, PrimeBot, MobyKingz and LSS Bot are local Windows/emulator bots that add a "cloud server" (a hosted Windows/RDP machine) or a "Farm for Me" managed service.
- **Purely local emulator bots:** ESB-TKR desktop, Ragebot TKR, Evonex, the GNBots desktop TKR bot, and EvonyLife's BotBoss.4000.
- **Open source:** I found no genuine open-source Evony TKR bot on GitHub.

### Cited Findings

#### A. Cloud-hosted bots (run on the vendor's servers, controlled from a browser or phone)

**1. Evony Auto (evonyauto.com)**
- Cloud bot managed from a browser. Advertised automations: boss rally auto-start/join, gathering, building and troop training — [Evony Auto](https://evonyauto.com/)
- **Login:** you enter the email you use for Evony, Evony emails you a 6-digit code, you type it in and pick which Monarchs (game accounts) to automate. No password is shared — [Evony Auto](https://evonyauto.com/)
- **Pricing (billed monthly):**
  - 24-hour free trial for 1 Monarch, no credit card
  - Starter: $49/mo for 3 Monarchs
  - Growth: $99/mo for 10 Monarchs
  - Scale: $149/mo for 25 Monarchs
  - Every paid plan unlocks every automation; tiers differ only by Monarch count — [Evony Auto](https://evonyauto.com/)
- **Development status / Discord size:** unknown. The site is live in 2026.

**2. EvonAI (evonai.app)**
- Cloud bot running 24/7. Advertised features — [EvonAI](https://evonai.app/):
  - auto-joins alliance rallies
  - leads your own boss rallies
  - scouts the whole map
  - tops up stamina
  - SVS enemy scanner
  - Discord alerts for boss spawns and SVS targets
  - controllable from a phone browser while the game is closed
- **Login:** enter your Evony email and receive a code; the vendor says linking takes under a minute — [EvonAI](https://evonai.app/)
- **Pricing:**
  - Solo $7.99/mo for 1 account
  - Squad $14.99/mo for 3 accounts
  - Fleet $26.99/mo for 8 accounts
  - 48-hour free trial; cancel before it ends and you are not charged — [EvonAI](https://evonai.app/)
  - A second snippet describes these as launch prices, with regular prices of $9.99 (Solo) to $29.99 (Fleet) — [EvonAI via search](https://evonai.app/)
- **Single-session limit:** the vendor notes Evony allows only one active session per account. Logging in yourself pauses the bot, and it reconnects and resumes after you log out — [EvonAI](https://evonai.app/)
- **ToS:** the vendor admits automation is against Evony's terms of service — [EvonAI](https://evonai.app/)
- No independent reviews found.

**3. GNBots "Evony Cloud Bot" (gnbots.com)**
- Runs from your browser with no emulator, download or PC required — [GNBots Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/)
- **Advertised features:**
  - map scanner
  - rallies, gathering, upgrades, shielding and daily tasks from a dashboard — [GNBots Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/)
  - "real-time auto shield" that activates a truce before enemy marches land — [GNBots via search](https://www.gnbots.com/auto/evony-cloud-bot/)
- **Login:** described as Game ID only, with no passwords or Gmail access — [GNBots via search](https://www.gnbots.com/auto/evony-cloud-bot/). A separate search could not confirm the Game ID linking detail, so treat it as unconfirmed.
- **Price:** not published.
  - A 2026 comparison lists the cloud price as "price not published", but gives the GNBots paid tier as ~$49/mo, ~$15/mo billed annually, or ~$175 lifetime, plus a "free-forever basic tier" — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
  - A free trial is advertised.
- **Promo video:** [YouTube: Evony Cloud Bot – No Downloads or Emulators Required](https://www.youtube.com/watch?v=kyH5r8AIgmM)

**4. ESB Cloud (Emulator Automation / Evony Smart Bot)**
- Hosted version of Evony Smart Bot. It runs on the vendor's servers and is controlled from a browser, including Safari on iPhone — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- **Pricing:** $5/mo for the first account ($6 with fee) and $3/mo for each additional account, labelled "introductory pricing". A 1-day trial is available — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- **Linking:** email code, or scanning a code in Evony (Settings > Account > Scan) — [ESB Cloud via search](https://www.emulatorautomation.com/evony-cloud-bot)
- **Features:** auto-join rallies, farm, and hunt bosses 24/7 with "no PC, no emulator and nothing to download" — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- **ToS:** the FAQ says bots are against Evony's ToS whether on a PC or in the cloud. ESB Cloud "keeps human-paced timing, but the risk is yours" — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- **Conflict:** a 2026 comparison says ESB-TKR "lacks cloud hosting options entirely" — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/). This is likely out of date relative to the ESB Cloud launch. The launch date is unknown.

**5. iScope Auto (auto.iscope.online), sister product of iScope Recon map intelligence**
- **Features:** rally joining with monster filters, resource gathering, peace-shield management and boss hunting — [iScope Auto](https://auto.iscope.online/)
- Described as running on a cloud Android device rather than your PC — [iScope Auto via search](https://auto.iscope.online/)
- **Rally setter:** auto-starts boss rallies on a schedule. It is included at no extra charge with any subscription of 3+ accounts, and it respects march slots so it doesn't block gathering or defense — [iScope Blog: Evony Rally Setter (2026)](https://www.iscope.online/blog/evony-rally-setter)
- **Pricing:** 1 account $10/mo; 3 accounts $20/mo; 6 accounts $30/mo; 50 accounts $150/mo — [iScope Auto](https://auto.iscope.online/)
- The parent platform, iScope Recon, sells map intelligence — [iScope Recon](https://www.iscope.online/)
- **Login method:** unknown.

**6. Fbots (fbots.org): multi-game vendor ("Viking Rise, Whiteout Survival & 18+ games")**
- Fbots says the bot doesn't run on the phone. It runs in the cloud or on a PC and is controlled from a browser — [Fbots Evony](https://fbots.org/en/evony-bot)
- **Features:** gathering (food, lumber, stone, ore, gems), building, research and troop training — [Fbots Evony](https://fbots.org/en/evony-bot)
- **Pricing (internally inconsistent):**
  - PC program: $1.5/account/mo (FAQ says from $1)
  - Shared server: $5/account/mo (FAQ says from $4)
  - VIP server: $9/account
  - Dedicated server: from $2/account/mo for 24–180 accounts
  - Free demo / free registration
  - Sources: [Fbots Evony](https://fbots.org/en/evony-bot); [Fbots home](https://fbots.org/en/)
- **Ban claim:** the vendor says "no bans have been recorded on our accounts" but doesn't guarantee it — [Fbots Evony](https://fbots.org/en/evony-bot)
- **Login method:** unknown.

#### B. Hybrid: a local bot plus a hosted "cloud server" or managed farming

**7. BoostBot (boostbot.org)**
- **Free Windows app:** unlimited accounts, basic settings only — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- **Premium:** $14.92/mo billed $179/year — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- **Bot Server:** $80/mo billed yearly. It is "hosted RDP with the license included" and "runs in our cloud", i.e. a hosted Windows machine, not a browser-native bot — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- **"Farm for Me"** managed service: from $8/account/mo — [BoostBot](https://boostbot.org/evony-kings-return-bot/). The comparison site gives $12/acct/mo — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- Cloud servers are marketed for Android, iOS and Mac users — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- **Features:** gather, building upgrades, train and heal, rallies, shield and quests. The script count is quoted as 29 (vendor) or 26 (comparison) — [BoostBot](https://boostbot.org/evony-kings-return-bot/); [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- **Refunds:** 24-hour money-back guarantee per one page; 14-day refund window on Premium per another — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- Page "last updated September 19, 2026" — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- **Promotional sister sites:** evonykingsreturnbot.com says "download and use the BoostBot software completely free" (Windows 10/11). It lists Premium at $25 and a cloud server at $80 for up to 60 accounts — [evonykingsreturnbot.com](https://evonykingsreturnbot.com/). autofarmbots.com carries a $25 price in its structured data and offers a "free version to download, or run it on a cloud Bot Server" — [AutoFarmBots](https://autofarmbots.com/evony-kings-return-bot/)

**8. PrimeBot (primebot.org)**
- Free version usable indefinitely with no account limits, plus Premium; also "a mobile plan that comes with a remote cloud server" (price not shown) — [PrimeBot](https://primebot.org/evony-the-kings-return-bot/)
- **Premium price conflict:** the shop lists $25/mo for Windows 10/11, with 1-, 6- and 12-month terms — [PrimeBot shop](https://primebot.org/shop/bots/evony-the-kings-return-bot/). A comparison lists a $15/mo Pro plan — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)

**9. MobyKingz (mobykingz.com)**
- Offers a PC version and a cloud-hosted "mobile version" on a remote server; claims unlimited accounts; support runs through Discord — [MobyKingz](https://mobykingz.com/pages/evony-the-kings-return-bot)
- Claims to be "the only working Evony TKR bot and cheat online", and its FAQ asks whether the bot can "hack diamonds" — [MobyKingz](https://mobykingz.com/pages/evony-the-kings-return-bot)
- **Pricing:** unknown.

**10. LSS Bot (lssbot.com)**
- Has an Evony TKR bot page — [LSS Bot](https://www.lssbot.com/evony-the-kings-return-bot/)
- A comparison says it offers free scripts and cloud hosting; its Farm-for-Me price is not published — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- Other details are unknown.

#### C. Local bots (PC/emulator)

**11. ESB-TKR (Evony Smart Bot; emulatorautomation.com / evonysmartbot.com, Vietnamese/English)**
- Automates rally joining, farming and boss workflows on Windows using Android emulators — [Emulator Automation](https://www.emulatorautomation.com/)
- The download page lists Windows and macOS — [ESB Download](https://www.emulatorautomation.com/Home/Download)
- Two interfaces (New UI and Original UI) share one subscription — [Emulator Automation](https://www.emulatorautomation.com/)
- **Pricing (desktop):**
  - $5/mo for 1 instance, $10/mo for 5, $20/mo for 15 (150k/300k/600k VND)
  - +$1 per extra instance beyond the "Farm 2" tier
  - Source: [ESB TKR payment page](https://www.evonysmartbot.com/p/payment.html)
- **Contradiction:** the FAQ says the bot does not run a subscription model and the full amount is due up front — [ESB TKR FAQ](https://www.evonysmartbot.com/p/faq.html)
- Promoted on the ESB-TKR YouTube channel, which carries a Discord invite — [ESB-TKR YouTube](https://www.youtube.com/channel/UCrS23MumH5VZQDyJkiG3DpA)
- Demo video: [Automatically Attack and Find Bosses using Evony Smart Bot](https://www.youtube.com/watch?v=J3IOhJ13pgo)
- Vendor docs and a 2026 blog are live — [ESB Docs](https://www.emulatorautomation.com/Documentation); [ESB Blog 2026](https://www.emulatorautomation.com/Blog/what-is-an-evony-bot)

**12. Ragebot TKR (rage.systems, by Rage Systems)**
- Emulator automation tool. Recommended emulator: MuMu Player, in portrait mode at 540×960 — [Ragebot Manual](https://rage.systems/manual/welcome.html)
- **Routines:**
  - Truce Agreement Renewal
  - Resource Gathering
  - Alliance Tile Gathering
  - Research Factory
  - Find Bosses
  - Start Rallies
  - Join Rallies
  - Source: [Ragebot TKR](https://rage.systems/)
- A comparison adds resource-tracking charts — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- Has an updates log — [Ragebot Updates](https://rage.systems/manual/updates.html); YouTube — [@RagebotTKR](https://www.youtube.com/@RagebotTKR)
- **Pricing:** unknown.

**13. Evonex (evonex.app)**
- Windows desktop bot. It reads the screen with computer vision and sends input over ADB — [Evonex](https://evonex.app/)
- Requires BlueStacks, MEmu, LDPlayer or MuMu set to exactly 540×960 portrait at 120 DPI — [Evonex Quick start](https://evonex.app/guide/quick-start)
- **Features:** rallies, gathering, troop training, daily activities, open boxes, recruit generals, City Mapper, and Coordex world-map scanning — [Evonex](https://evonex.app/); [Open Boxes guide](https://evonex.app/guide/task-open-boxes); [Recruit Generals guide](https://evonex.app/guide/lib-recruit)
- **Version:** 0.1.0 — [Evonex Download](https://evonex.app/download)
- **Pricing conflict:** one page says it is free in beta with every feature and unlimited instances. Another describes paid Boss Radar seats per server for each 30-day period — [Evonex](https://evonex.app/); [Boss Radar](https://bossradar.app/)
- Collects only your sign-in email and instance details; disclaims any affiliation with Top Games — [Evonex](https://evonex.app/)
- Promo video: [Introducing Evonex](https://www.youtube.com/watch?v=NfIc0aEI7fc)

**14. GNBots Evony TKR Bot (desktop/app product, separate from the cloud bot)**
- Auto-joins boss rallies, farms tiles and completes daily tasks on PC, Android, Mac and iOS — [GNBots Evony TKR Bot](https://www.gnbots.com/shop/evony-tkr-bot/)
- Also advertises troop training, healing and reward collection — [GNBots](https://gnbots.com/auto/evony-bot/)
- Claims "humanized clicking" as anti-ban technology and "100% Working in 2026" — [GNBots Evony TKR Bot](https://www.gnbots.com/shop/evony-tkr-bot/)

**15. EvonyLife "BotBoss.4000" (evonylife.com)**
- Free Windows 10/11 rally-joining bot for up to 4 accounts. Requires an emulator (BlueStacks, MEmu, LD Player or Nox); labelled beta, v1.022 — [EvonyLife](https://evonylife.com/); [Instructions](https://evonylife.com/instructions-for-use/); [BlueStacks setup](https://evonylife.com/help-to-setup-evony-account-on-bluestacks/)
- The search summary flagged that some setup details date back several years. The current activity status is uncertain.

**16. Unidentified vendor:** a YouTube tutorial titled "How to use Evony BOT … sign up free 3 days, auto rally join and auto boss hunt" — [YouTube](https://www.youtube.com/watch?v=ShVC8wkZOOs). The vendor could not be identified from the snippet.

#### D. Adjacent tools (not gameplay automation)

**Official first-party option**
- Evony's own Rally Monthly Card costs $9.99 and lasts a month, with caps on offline rally joining. A roughly two-year-old review says it does not allow setting rallies — [Theria Games](https://theriagames.com/guide/evony-rally-monthly-card-guide/)

**Discord intel and helper bots**
- KeepScout: paid, alliance-focused live battlefield intel pushed to Discord. It says it does not automate gameplay; free entry tier — [KeepScout](https://www.keepscout.com/)
- EvonyCompanion: a Discord bot plus a community server — [EvonyCompanion](https://evonycompanion.com/community)
- "Evony Bot" on top.gg: a calculator for speed-ups and resource/power gains — [top.gg](https://top.gg/bot/970331727526522900)

**Alliance management**
- EvonyTools Alliance Studio: roster, events and rally coordination. It signs in with Discord OAuth and never asks for Evony credentials. It has a free tier plus three paid plans; one page labels it "free while in beta" — [Alliance Studio](https://studio.evonytools.com/); [Credential Safety](https://docs.evonytools.com/credential-safety)

**Map intelligence**
- iScope Recon — [iScope](https://www.iscope.online/)
- Boss Radar (shares an account with Evonex) — [Boss Radar](https://bossradar.app/)

#### E. Historical or stale entries
- OwnedCore and elitepvpers sales threads, "Evony The King's Return Bot – Auto Farm Unlimited Accounts" (~2022–2023, GNBots-style marketing copy) — [OwnedCore](https://www.ownedcore.com/forums/mmo/mobile-flash-game-hacks/994231-evony-kings-return-bot-auto-farm-unlimited-accounts-evony-tkr-bot.html); [elitepvpers 5161019](https://www.elitepvpers.com/forum/mobile-games-trading/5161019-evony-kings-return-bot-auto-farm-unlimited-accounts-evony-tkr-bot.html); [elitepvpers 5062468](https://www.elitepvpers.com/forum/mobile-games-trading/5062468-auto-farm-bot-evony-kings-return.html)
- A 2016 blog on using "roboevony" had players enter their Evony email and password directly into the bot — [joevony blog, 2016](https://joevony.wordpress.com/2016/03/12/using-a-bot/)
- "Evony-bot" from Travianbot.com, described as an unofficial automation assistant for Evony and probably aimed at the classic browser game — [Software Informer](https://evony-bot.software.informer.com/)

#### F. GitHub / open source
- A GitHub search turned up no genuine Evony TKR automation repository. The hits were for other games (Grepolis autofarm, TravianBotSharp) and spam pages — [search result: rafalohaki/autofarm](https://github.com/rafalohaki/autofarm)

#### Summary comparison table (all figures vendor-advertised unless noted)

| Bot | Hosting | How it reaches your account | Entry price | Accounts | Trial | Sources |
|---|---|---|---|---|---|---|
| Evony Auto | Cloud (browser) | Evony email + 6-digit code | $49/mo | 3 / 10 / 25 by tier | 24 h, 1 Monarch | [link](https://evonyauto.com/) |
| EvonAI | Cloud (browser/phone) | Evony email + code | $7.99/mo (launch) | 1 / 3 / 8 | 48 h | [link](https://evonai.app/) |
| GNBots Evony Cloud Bot | Cloud (browser) | "Game ID only" (unconfirmed) | Not published | Unknown | Yes | [link](https://www.gnbots.com/auto/evony-cloud-bot/) |
| ESB Cloud | Cloud (browser, iPhone Safari) | Email code or in-game QR scan | $5 first + $3 each | Per account | 1 day | [link](https://www.emulatorautomation.com/evony-cloud-bot) |
| iScope Auto | Cloud Android device | Unknown | $10/mo | 1 / 3 / 6 / 50 | Unknown | [link](https://auto.iscope.online/) |
| Fbots | Cloud servers or PC program | Unknown | $1–1.5/acct (PC); $4–5/acct (server) | Up to 180 (dedicated) | Free demo | [link](https://fbots.org/en/evony-bot) |
| BoostBot | Local Windows + hosted RDP + managed farming | Emulator on local or hosted Windows | Free; Premium $179/yr; Server $80/mo (yearly); Farm for Me from $8/acct | "Unlimited" (60 cap per one sister site) | 24 h money-back or 14-day refund (conflicting) | [link](https://boostbot.org/evony-kings-return-bot/) |
| PrimeBot | Local + mobile cloud plan | Emulator | Free; Premium $15–25/mo (conflicting) | No limit on free tier | Free tier | [link](https://primebot.org/evony-the-kings-return-bot/) |
| MobyKingz | Local + cloud mobile version | Unknown | Unknown | "Unlimited" | Unknown | [link](https://mobykingz.com/pages/evony-the-kings-return-bot) |
| LSS Bot | Local + cloud (per comparison) | Unknown | Free scripts (per comparison) | Unknown | Unknown | [link](https://bestmobilebots.com/evony-kings-return-bot/) |
| ESB-TKR desktop | Local (Windows/macOS + emulator) | Emulator | $5/mo for 1 instance | 1 / 5 / 15 instances | Unknown | [link](https://www.evonysmartbot.com/p/payment.html) |
| Ragebot TKR | Local (MuMu emulator) | Emulator | Unknown | Unknown | Unknown | [link](https://rage.systems/) |
| Evonex | Local (Windows + emulator, CV + ADB) | Emulator | Free in beta (Boss Radar paid) | Unlimited instances | Free beta | [link](https://evonex.app/) |
| GNBots TKR Bot | Local (PC/Android/Mac/iOS) | Emulator/device | Comparison: free basic; ~$49/mo or ~$175 lifetime | Unknown | Free trial | [link](https://www.gnbots.com/shop/evony-tkr-bot/) |
| EvonyLife BotBoss.4000 | Local (Windows + emulator) | Emulator | Free (beta) | Up to 4 | n/a | [link](https://evonylife.com/) |

### Inferences
- The "true cloud" segment is crowded with small or new vendors whose pages describe 2026 features: Evony Auto, EvonAI, ESB Cloud, iScope Auto and Evonex's Boss Radar. All of them use email-code account linking, apparently because Evony itself offers email verification, QR login and single-session play. Older multi-game vendors (BoostBot, PrimeBot, GNBots, LSS Bot) mostly offer "cloud" as a hosted Windows/emulator machine or as managed farming, not a browser-native bot.
- Per-account cost varies roughly 10x. Cheapest cloud: ESB Cloud ($3–5/acct) and Fbots shared server ($4–5/acct). Mid: EvonAI (~$3.4–8/acct) and iScope (~$3–10/acct). Most expensive per account: Evony Auto (~$6–16/acct).
- The email-code login hands the vendor a live game session. The vendor therefore effectively controls the account while linked, even though no password is shared. This is inferred from the linking mechanism, not stated by the vendors.

### Gaps
- I could not read pages directly (DNS blocked for evonyauto.com, evonai.app, gnbots.com and fbots.org), so tier contents, fine print and dates are from search snippets only.
- Unknown for most vendors: Discord member counts, last-update dates (except BoostBot, updated 2026-09-19), company ownership and jurisdiction.
- Login method unknown for iScope Auto, Fbots, MobyKingz, LSS Bot and PrimeBot cloud.
- GNBots cloud pricing unconfirmed; Ragebot and MobyKingz pricing unknown.
- ESB Cloud launch date unknown.

## Q2. Which bots are most recommended or discussed by players in 2025–2026?

### Takeaway
I found no independent player consensus. Reddit (r/Evony, r/EvonyTKR) was inaccessible to the search tools, and the visible "rankings" come from affiliate-style comparison pages.
- **Most externally reviewed:** GNBots (~796 Trustpilot reviews) and BoostBot (~18 Trustpilot reviews).
- **Most visible Evony-only specialists:** ESB-TKR and Ragebot TKR (dedicated YouTube channels).
- **Cloud newcomers (EvonAI, Evony Auto, iScope Auto):** no independent reviews found.

### Cited Findings
- **BestMobileBots comparison (updated August 2026)** — [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/):
  - Compares 7 providers.
  - Ranks BoostBot "top overall pick for Evony TKR in 2026" (26 scripts, 24-hour money-back).
  - Names ESB-TKR the specialist pick, Ragebot TKR the "second Evony-only specialist", and GnBots the best free option.
  - This verdict matches BoostBot's own marketing copy, so treat it as possibly affiliate-driven.
- **GNBots on Trustpilot:** 796 reviews; the TrustScore varies by snapshot (~3.9–4.2). GNBots' own site claims 4.7 from 500+ reviews — [Trustpilot GnBots](https://www.trustpilot.com/review/www.gnbots.com)
  - Evony-specific praise: shielding all farms takes "about 30 minutes … rather than a couple hours" — [Trustpilot GnBots](https://www.trustpilot.com/review/www.gnbots.com)
- **BoostBot ratings disagree across sources:**
  - About 18 Trustpilot reviews averaging 2 stars in one snapshot. One reviewer: "There is so much the Bot is not doing so I have to manually do loads" — [Trustpilot boostbot.org](https://nz.trustpilot.com/review/boostbot.org)
  - Realreviews.io lists 4.4 from 7 reviews — [RealReviews](https://realreviews.io/reviews/boostbot.org)
  - BoostBot cites 3.8/5 from 15 reviews on its own blog — [BoostBot "Is BoostBot legit?"](https://boostbot.org/blog/is-boostbot-legit/?v=0dbe4fb2d698)
- **YouTube presence (Evony-specific):**
  - ESB-TKR channel — [YouTube](https://www.youtube.com/channel/UCrS23MumH5VZQDyJkiG3DpA)
  - Ragebot TKR channel — [YouTube](https://www.youtube.com/@RagebotTKR)
  - GNBots cloud bot promo — [YouTube](https://www.youtube.com/watch?v=kyH5r8AIgmM)
  - Evonex intro — [YouTube](https://www.youtube.com/watch?v=NfIc0aEI7fc)
- **Official community context:** the official Evony TKR Discord shows roughly 147,000–150,000 members on listing sites — [Discord Bot List](https://discordbotlist.com/servers/evony-the-king-s-return-909673086465507358). I found no evidence that bot vendors are discussed or endorsed there.
- **Partnership:** an EvonyCompanion "Partners" page surfaced in the ESB search results, but its content could not be confirmed — [EvonyCompanion Partners](https://evonycompanion.com/partners)

### Inferences
- **Most mature and visible:** GNBots and BoostBot, both multi-game vendors with large review footprints and many years of Evony marketing (copy appears on forums from 2022–2023).
- **Evony specialists:** ESB-TKR and Ragebot appear to be the Evony-only tools with the most dedicated content.
- **Newer cloud entrants:** EvonAI, Evony Auto, iScope Auto, ESB Cloud and Evonex have little or no independent footprint yet.

### Gaps
- Reddit r/Evony and r/EvonyTKR are blocked to the search tool, so I could not measure frequency of mentions or player sentiment there.
- I found no Evony forum threads or disboard/top.gg listings for automation-vendor Discords, and no member counts.
- No Trustpilot pages were found for Evony Auto, EvonAI, iScope, Fbots, Ragebot, ESB or Evonex.

## Q3. What core feature sets does each bot advertise?

### Takeaway
- **Rally automation is the headline everywhere:** auto-join boss rallies, and increasingly auto-start or "set" boss rallies on a schedule.
- **Next most common:** gathering/tile farming, building and research upgrades, troop training/healing, and shield/truce renewal.
- **Cloud newcomers differentiate on:** map/boss scanning, SVS enemy scanning and Discord alerts.
- **Resource transfer to a main account:** none of the sources I found advertises it explicitly.

### Cited Findings

**Rally joining and starting**
- Evony Auto (auto-start/join) — [Evony Auto](https://evonyauto.com/)
- EvonAI (join, and lead your own boss rallies) — [EvonAI](https://evonai.app/)
- iScope (join with monster filters; scheduled rally setter) — [iScope Auto](https://auto.iscope.online/); [iScope blog](https://www.iscope.online/blog/evony-rally-setter)
- ESB / ESB Cloud — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- Ragebot (Start and Join Rallies) — [Ragebot](https://rage.systems/)
- GNBots — [GNBots TKR](https://www.gnbots.com/shop/evony-tkr-bot/)
- BoostBot — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- Evonex — [Evonex](https://evonex.app/)
- EvonyLife (rally-join only) — [EvonyLife](https://evonylife.com/)

**Monster/boss finding and map scanning**
- EvonAI (map scouting, SVS enemy scanner) — [EvonAI](https://evonai.app/)
- GNBots Cloud (map scanner) — [GNBots Cloud](https://www.gnbots.com/auto/evony-cloud-bot/)
- Ragebot (Find Bosses) — [Ragebot](https://rage.systems/)
- Evonex (Coordex world-map scanning; Boss Radar) — [Evonex](https://evonex.app/); [Boss Radar](https://bossradar.app/)
- iScope (boss hunting) — [iScope Auto](https://auto.iscope.online/)
- ESB (boss hunting) — [ESB YouTube demo](https://www.youtube.com/watch?v=J3IOhJ13pgo)

**Gathering and tile farming**
- Evony Auto — [Evony Auto](https://evonyauto.com/)
- iScope — [iScope Auto](https://auto.iscope.online/)
- Fbots (food, lumber, stone, ore, gems) — [Fbots](https://fbots.org/en/evony-bot)
- Ragebot (Resource and Alliance Tile Gathering) — [Ragebot](https://rage.systems/)
- GNBots (farms tiles) — [GNBots TKR](https://www.gnbots.com/shop/evony-tkr-bot/)
- BoostBot — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- Evonex — [Evonex](https://evonex.app/)

**Building and research upgrades**
- Evony Auto (building) — [Evony Auto](https://evonyauto.com/)
- Fbots (building, research) — [Fbots](https://fbots.org/en/evony-bot)
- Ragebot (Research Factory) — [Ragebot](https://rage.systems/)
- BoostBot (building upgrades) — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- GNBots Cloud ("upgrades") — [GNBots Cloud](https://www.gnbots.com/auto/evony-cloud-bot/)

**Troop training and healing**
- Evony Auto — [Evony Auto](https://evonyauto.com/)
- Fbots — [Fbots](https://fbots.org/en/evony-bot)
- BoostBot (train and heal) — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- GNBots (training, healing) — [GNBots](https://gnbots.com/auto/evony-bot/)
- Evonex — [Evonex](https://evonex.app/)

**Shield, truce and defense**
- iScope (peace-shield management) — [iScope Auto](https://auto.iscope.online/)
- GNBots Cloud (real-time auto shield that triggers a truce before enemy marches land) — [GNBots Cloud](https://www.gnbots.com/auto/evony-cloud-bot/)
- Ragebot (Truce Agreement Renewal) — [Ragebot](https://rage.systems/)
- BoostBot (shield) — [BoostBot](https://boostbot.org/evony-kings-return-bot/)

**Daily tasks, quests and rewards**
- GNBots — [GNBots TKR](https://www.gnbots.com/shop/evony-tkr-bot/)
- BoostBot (quests) — [BoostBot](https://boostbot.org/evony-kings-return-bot/)
- Evonex (daily activities, open boxes, recruit generals) — [Evonex](https://evonex.app/)

**Stamina top-up and Discord alerts**
- EvonAI — [EvonAI](https://evonai.app/)

**Alliance help, resource transfer to main, auto-defense beyond shielding**
- Not found in any of the summaries I retrieved for any vendor.

### Inferences
- Rally automation, especially boss rallies, is the core value in 2025–2026. This matches player complaints about 24/7 bot-run boss rallies on servers (see Q4) and the existence of Evony's own paid Rally Monthly Card — [Theria Games](https://theriagames.com/guide/evony-rally-monthly-card-guide/)
- Cloud bots that use the game's own session (EvonAI, Evony Auto) may work at the protocol or session level rather than by screen-scraping. This is unconfirmed; ESB Cloud says it runs "Evony Smart Bot on our servers", i.e. likely an emulator in the cloud.

### Gaps
- Full feature matrices, per-feature tier gating and alliance-help/resource-transfer support could not be verified without direct page access.
- It is unknown whether any cloud bot supports farm-to-main resource transfer.

## Q4. Are there notable red flags (password sharing, payment disputes, scams, malware, account theft, bans)?

### Takeaway
- **Biggest structural risk:** Evony's terms explicitly ban bots and automation, and vendors themselves concede it. Any bot use risks sanctions, though enforcement appears inconsistent.
- **No vendor confirmed as a scam or shut down:** I found no 2025–2026 report of any of the vendors above being a confirmed scam or shutting down.
- **Warning signs:**
  - pricing that contradicts itself across a vendor's own pages
  - affiliate-style "comparison" and sister sites
  - "cheat/hack diamonds" marketing (MobyKingz)
  - unverifiable "never banned" claims
  - gem-generator and leaked-credential spam pages around the Evony keyword

### Cited Findings

**ToS prohibition**
- Top Games terms (dated March 4, 2025 per search summary) bar using "cheats, exploits, automation software, bots, hacks, mods or any unauthorized third-party software" — [Evony Terms of Service](https://m.evony.com/Terms.html)
- The terms also say the games may monitor RAM and CPU processes for unauthorized third-party programs — [Evony Terms](https://m.evony.com/Terms.html) (the clause was quoted in a community write-up)
- Near-identical language appears in the Evony Mobile (uCool) terms — [Evony Mobile Terms](https://em.evony.com/index.php?r=home%2FshowTermsOfService)

**Vendors acknowledge the ToS risk**
- EvonAI — [EvonAI](https://evonai.app/)
- ESB Cloud ("bots are against Evony's ToS, on a PC or in the cloud … the risk is yours") — [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- Evonex ("Automating a game carries account risk") — [Evonex Download](https://evonex.app/download)
- ESB's blog says the game does ban accounts it believes are automated, yet also claims there is "no direct proof of a ban relating to Evony Bots" — [ESB Blog](https://www.emulatorautomation.com/Blog/what-is-an-evony-bot)

**Enforcement anecdotes**
- A Q&A page describes a 3-day rally ban after a player was reported for alleged bot use (anecdotal) — [JustAnswer](https://www.justanswer.com/software/s9gqc-banned-evony-newd-know.html)
- Trustpilot reviews of Top Games say a player complained for over a year about third-party software on server 745 running boss-monster rallies 24/7, and admins struggled to prove bot farms. Another review blames bots on S534 — [Trustpilot topgamesinc.com](https://ca.trustpilot.com/review/topgamesinc.com); [Trustpilot evony.com](https://www.trustpilot.com/review/www.evony.com)

**Unverifiable "no ban" claims**
- GNBots: "We have never had a player banned" — [GNBots TKR](https://www.gnbots.com/shop/evony-tkr-bot/)
- Fbots: "no bans have been recorded on our accounts" — [Fbots](https://fbots.org/en/evony-bot)

**Credentials and account control**
- Evony Auto, EvonAI and ESB Cloud link by email code (ESB also by in-game QR scan), not by password — [Evony Auto](https://evonyauto.com/); [EvonAI](https://evonai.app/); [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)
- GNBots Cloud claims "Game ID only, no passwords or Gmail access" — [GNBots Cloud](https://www.gnbots.com/auto/evony-cloud-bot/)
- Older bots such as roboevony (2016) required entering your Evony email and password — [joevony blog](https://joevony.wordpress.com/2016/03/12/using-a-bot/)
- Evony allows one session per account, so cloud bots and the player kick each other off — [EvonAI](https://evonai.app/)

**Scam-adjacent spam**
- Bandcamp-hosted "Evony The King's Return gems generator 2024" pages — [Bandcamp spam](https://kifteo.bandcamp.com/album/new-tool-evony-the-kings-return-gems-generator-tools-version-update-generator-2024-no-password-and-human-verification-ooe)
- A freeaccount.biz page listing what appear to be leaked Evony email/password pairs — [freeaccount.biz](https://freeaccount.biz/accounts/evony.com)

**"Cheat" marketing**
- MobyKingz calls itself "the only working Evony TKR bot and cheat online" and its FAQ addresses "hack diamonds" — [MobyKingz](https://mobykingz.com/pages/evony-the-kings-return-bot)

**Pricing and terms inconsistencies**
- Fbots: $1 vs $1.5 (PC) and $4 vs $5 (server) — [Fbots](https://fbots.org/en/evony-bot)
- PrimeBot: $15 vs $25 — [PrimeBot shop](https://primebot.org/shop/bots/evony-the-kings-return-bot/); [BestMobileBots](https://bestmobilebots.com/evony-kings-return-bot/)
- BoostBot: $14.92/mo vs $25; "unlimited" vs a 60-account cap; 26 vs 29 scripts; 24 h vs 14-day refund — [BoostBot](https://boostbot.org/evony-kings-return-bot/); [evonykingsreturnbot.com](https://evonykingsreturnbot.com/)
- ESB: subscription vs "no subscription, full amount up front" — [ESB FAQ](https://www.evonysmartbot.com/p/faq.html); [ESB payment](https://www.evonysmartbot.com/p/payment.html)
- Evonex: free beta vs paid seats — [Evonex](https://evonex.app/)

**Customer-service complaints**
- GNBots Trustpilot negatives include a long-term customer saying the bot "force closes and doesn't do anything after the first few months" with poor support, another calling the company "ruthless and insensitive to their customers", and a truncated review headlined "After canceling subscription same day…" — [Trustpilot GnBots](https://www.trustpilot.com/review/www.gnbots.com)
- BoostBot's Trustpilot shows a 2-star average in one snapshot — [Trustpilot boostbot.org](https://nz.trustpilot.com/review/boostbot.org)

**Shutdowns and confirmed scams**
- No 2026 evidence of any Evony bot being discontinued or confirmed as a scam. Searches returned only live vendor pages — [search summary incl. BoostBot](https://boostbot.org/evony-kings-return-bot/); [ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot)

### Inferences
- **Safer login model, same ban exposure:** the email-code / QR linking used by cloud bots avoids sharing passwords, but it still gives a third party a live, persistent session on the account. A compromised or malicious vendor could act in-game (spend resources, move troops). The ToS ban risk is the same as for local bots.
- **Local bots carry different risks:** they keep credentials on the user's machine, but they mean installing unsigned third-party Windows software (malware risk). The ToS clause on RAM/CPU monitoring suggests the client could in principle detect locally running automation, which is not a concern for server-side cloud bots.
- **Cloud vs ToS clause:** the clause targets "software designed to modify or interfere", so cloud bots are no more compliant than local ones, as ESB itself concedes.

### Gaps
- I found no documented account thefts, malware reports, chargebacks or payment disputes tied specifically to any named Evony TKR bot vendor.
- I found no official Top Games ban-wave announcements for 2025–2026.
- Reddit threads, the most likely source for such reports, could not be searched.
