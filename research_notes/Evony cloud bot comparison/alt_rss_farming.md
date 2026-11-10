# Alt / Farm Account RSS Maximization in Evony: The King's Return and Multi-Account Bots

Research date: 2026-11-10. **Method caveat for the report writer:** WebFetch could not reach evonyguidewiki.com, evonytkr.com or gnbots.com from this session (host not allowed in the session's network settings), so every finding below comes from web-search result summaries, not full-page reads. Exact numbers should be re-checked against the full pages or in-game before publication. Where a search summary did not say which of several listed pages a claim came from, I say so.

## Q1. Mechanics: how RSS moves from an alt to a main (transport, Embassy, fees, caps, Family Group, plundering)

### Takeaway
In current TKR, the official way to move RSS is **Embassy-based transport to an alliance member**. The **Family Group** feature (introduced around 2024) explicitly makes resource exchange between linked accounts, including transport, plundering and Royal Waybills, "not considered violations." Transport still has a fee. A community source puts the fee at 60% at Embassy L1 falling to 15% at L30+. The Embassy level also sets the daily transport count and the receive cap. Exact per-level tables were not found.

### Cited Findings
- **Official Top Games Inc. rules for Family Group sharing.** Both players must be in the same alliance, the daily transport limit must not have been hit, and Embassy level requirements must be met. "The Embassy level determines both the maximum number of daily transports and the maximum amount of resources that can be received from alliance members." — [Top Games Inc. – Conditions for Sharing Resources Within a Family Group](https://info.topgamesinc.com/docs/evonytkr/conditions-for-sharing-resources-within-a-family-group/) (official publisher doc; page date not shown in search snippet)
- **Transported resources are NOT protected** and do not count as safe resources, so they can be plundered from the main after arrival. — [Top Games Inc. – Conditions for Sharing Resources](https://info.topgamesinc.com/docs/evonytkr/conditions-for-sharing-resources-within-a-family-group/)
- **Transport fees still apply inside a Family Group.** — [Top Games Inc. – Conditions for Sharing Resources](https://info.topgamesinc.com/docs/evonytkr/conditions-for-sharing-resources-within-a-family-group/); [Top Games Inc. – Family Group Feature Announcement](https://info.topgamesinc.com/evony-family-group-feature-announcement/)
- **Officially sanctioned transfer methods.** Per the official announcement text, resource exchange between Family Group members "regardless of the method" is not a violation. The term covers all previous transfer methods, "including—but not limited to—transportation, plundering, and Royal Waybills." This means hitting your own farm with your main ("RSS banking" by plunder) is sanctioned for Family Group members. — [Top Games Inc. – Family Group Feature Announcement](https://info.topgamesinc.com/evony-family-group-feature-announcement/); summarized in [Theria Games – Family Group Feature Announcement](https://theriagames.com/evony-family-group-feature-announcement/)
- **Family Group structure.**
  - A group cannot be deleted once created, and links between accounts cannot be removed.
  - The number of members you can add depends on VIP level, added one at a time.
  - Invitations expire if not accepted.
  - Members on different servers cannot send items to each other.

  Sources: [Theria Games – Evony Family Group Guide](https://theriagames.com/guide/evony-family-group-guide/) (about 2 years old, so roughly late 2024); [Top Games Inc. – Family Group Feature Announcement](https://info.topgamesinc.com/evony-family-group-feature-announcement/)
- **Fee by Embassy level.** The fee runs "from 60% at level 1, to 15% at level 30+." — [Theria Games – Evony Family Group Guide](https://theriagames.com/guide/evony-family-group-guide/) (community source, about 2 years old; not confirmed against an official table)
- **What upgrading the Embassy does.** It raises the amount and number of resources that can be sent and received, and it lowers transport fees. — [Theria Games – Evony Embassy Guide](https://theriagames.com/guide/evony-embassy-guide/)
- **The same, from the TKR guide wiki.** A higher Embassy level increases "the amount of resources that can be transported, Number of times, Amount of resources that can be received" and decreases the "Rate of transport fees." Academy research and the Alliance tech category also help. — [Evony Guide Wiki – Embassy](https://evonyguidewiki.com/en/embassy-en/) (search snippet only; page not fetchable)
- **Embassy unlock and prerequisite.**
  - The Embassy unlocks at Keep L9, and upgrading it decreases the tax on sending resources to alliance members — [Evony TKR Fandom – Buildings](https://evony-the-kings-return.fandom.com/wiki/Buildings)
  - The Market must be upgraded before the Embassy — [Evony TKR Fandom – Embassy](https://evony-the-kings-return.fandom.com/wiki/Embassy)
- **Keep the Embassy near Keep level.** One guide recommends this, mainly in the context of alliance help. — [EvonyTKRGuide – How To Use Alliance Help](https://www.evonytkrguide.com/guides/evony-tkr-guide-how-to-use-alliance-help)
- **Alliance-only transport (historical).** Resources cannot be sent to players in another alliance. This comes from the classic-Evony Fandom wiki (about 609 days old) and is not TKR-specific. It matches the TKR "same alliance" rule above. — [Evony Wiki (classic) – Q&A](https://evony.fandom.com/wiki/Questions_and_Answers)
- **Royal Waybills from the alt.** A historical 2018 alt guide says you can send resources to the main with waybills, which come from smashing the "6 egg" on the alt. — [EvonyTKR.com – Server Wars: Setting up an Alt (2018-08-18)](https://evonytkr.com/2018/08/18/server-wars-setting-up-an-alt/) (search snippet; **historical**)
- **Market and gold.** A YouTube comment says that at Market L30 or below you can buy RSS with gold, but above L30 you can't. This is an unverified user comment. — [YouTube – Evony Farm Accounts Explained](https://www.youtube.com/watch?v=DJvBTmcDxp4)
- **Plunder limits on low keeps.** A user comment on the wiki says taking resources from a low-keep account is limited. It is not an official rule. — [Evony TKR Fandom – Warehouse](https://evony-the-kings-return.fandom.com/wiki/Warehouse)
- **Warehouse protection.** The Warehouse protects a capped amount of resources from plunder, the cap rises with level, and it needs Keep L14. — [Evony TKR Fandom – Warehouse](https://evony-the-kings-return.fandom.com/wiki/Warehouse)

### Inferences
- The **Embassy is the key transfer building on both ends**. The farm's Embassy sets how much and how often it can send, and the fee. The main's Embassy sets how much it can receive per day. The fee falling from about 60% to about 15% means a farm under Embassy L30 loses a large share of what it sends.
- **Plundering your own farm with the main** is now explicitly allowed for Family Group members. It may sidestep the transport fee or daily send count, but the publisher sources do not say this, so treat it as unconfirmed. On the farm, a low Warehouse leaves more resources unprotected and therefore takeable by the main, but the same is true for enemies.
- Because transported RSS lands **unprotected** on the main, players should move it just before spending it, or keep the main shielded.
- The **Family Group cap is tied to VIP level**, so the number of alts that can be formally linked to one main is limited by the main's VIP. Alts outside the Family Group fall back to plain alliance transport, which the sources do not show as protected from multi-account enforcement.

### Gaps
- Exact per-level tables were not found for the Embassy fee %, daily transport count, per-transport load, or receive cap (the guide-wiki page could not be fetched).
- How many Family Group members each VIP level allows: not found.
- Whether plunder or Royal Waybill transfers bypass the transport fee or daily caps: unknown.
- Whether the "Trading Post"/Market plays any role in TKR alt-to-main transfer: the searches suggest the Embassy, not a Trading Post, handles transport. The Trading Post/tax figures in searches came from Rise of Kingdoms and were excluded.
- Royal Waybill current sources and caps: only a 2018 source was found.

## Q2. Farm-account setup that maximizes RSS/day

### Takeaway
Community guidance converges on these points:
- Max out resource buildings (farms, sawmills, quarries, mines).
- Raise the Keep only when needed to unlock building levels, but keep the Embassy high for transport.
- Gather on the highest tile level the march can handle.
- Stack gathering-speed and load boosts: general skills, talents, and Keep level, which slightly raises tile gather speed.

Published daily figures range from about 300–400M RSS/day (community guide, unspecified account type) to a vendor's unverified "4B/day" bot claim.

### Cited Findings
- **Build priorities for a farm.** Farms, sawmills, quarries and mines are "your main source of resources" and should always be upgraded as high as possible. Upgrade the Keep and Walls only when required to unlock more building levels. — [AVTech Guides – Evony Farm Account Leveling Guide](https://evony.avtechguides.com/evony-farm-account-leveling-guide/) (date not shown in snippet)
- **Maximum farms on the alt (historical).** A 2018 alt guide says to build the maximum number of farms so the alt keeps producing food during SvS/KE without gathering. It also says to pick a secluded map spot and be ready to bubble (shield) both accounts if someone ports in. — [EvonyTKR.com – Setting up an Alt (2018-08-18)](https://evonytkr.com/2018/08/18/server-wars-setting-up-an-alt/) (**historical**)
- **Tile level.** "Always aim for the highest-level resource tiles your march can handle efficiently." — [BlueStacks – ETKR Resource Farming Guide](https://www.bluestacks.com/blog/game-guides/evony-the-kings-return/etkr-resource-farming-guide-en.html)
- **Keep level and gather speed.** Raising the Keep slightly increases gather speed. The example given is about 156,000/hour at Keep 33 vs about 158,000/hour at Keep 34. The search summary did not say which page this came from; it was likely [Evony Guide Wiki – How to get Resources Efficiently](https://evonyguidewiki.com/en/how-to-get-resource-en/), otherwise [AVTech Guides](https://evony.avtechguides.com/evony-farm-account-leveling-guide/).
- **Gathering boosts.**
  - The Jungle buff adds +10% gathering speed.
  - The Queen of Silla general adds +20% extra resources from gathering.
  - A gathering talent upgraded four times adds +20% gathering bonus from resource spots.

  Source: [MMO Culture – Evony TKR Resource Optimization Guide](https://mmoculture.com/tips-guides/evony-the-kings-return-resource-optimization-guide/)
- **Daily gathering potential.** Players can gather "millions of resources per hour" and "upwards of three to four hundred million of resources per day." — [EvonyTKRGuide – Guide to Gathering Resources](https://www.evonytkrguide.com/guides/evony-tkr-guide-to-gathering-resources) (account type, march count and buffs not specified)
- **Embassy level.** Keep it close to Keep level. — [EvonyTKRGuide – Alliance Help](https://www.evonytkrguide.com/guides/evony-tkr-guide-how-to-use-alliance-help)
- **Market before Embassy.** The Market must be upgraded before the Embassy. — [Evony TKR Fandom – Embassy](https://evony-the-kings-return.fandom.com/wiki/Embassy)
- **Shared tile queue (ESB bot).** The ESB TKR bot's farming guide describes choosing tile levels and types, and a "Send To Collective" queue that shares found tiles among users. Only L15 tiles are shared to the collective, which implies L15 is the top tile level being farmed. — [ESB TKR – Farming Guide (Feb 2022)](https://www.evonysmartbot.com/2022/02/farming-guide.html); [ESB TKR – Collective Guide for Farming (Feb 2022)](https://www.evonysmartbot.com/2022/02/collective-guide-for-farming.html)
- **Farm-production upgrade table.** The Evony Guide Wiki "Farm" page has Keep requirements, times and costs per level, but its contents could not be fetched. — [Evony Guide Wiki – Farm](https://evonyguidewiki.com/en/farm-en/)

### Inferences
- An RSS-maximizing farm looks like this:
  - Max resource buildings for passive production.
  - Gathering marches on L15 tiles (or the highest the march load can clear).
  - A gathering general such as Queen of Silla, plus gathering talents.
  - Embassy pushed toward L30+ to bring the transport fee down to about 15%.
  - The Market upgraded alongside it, since it is a prerequisite.
- **Gathering usually dominates passive building production** at scale. That is why bots focus on auto-gather and tile-level selection. The per-hour figures above (about 156k/hour per tile at Keep 33) suggest per-march yield is modest, so march count and uptime (24/7 automation) are the main multipliers.
- **Trade-off on Keep level.** A higher Keep gives slightly faster gathering and more marches, but costs RSS and time to reach. Guides suggest raising the Keep only for unlocks.

### Gaps
- No current (2025–2026) source gave a recommended farm Keep level. Common community targets such as K15–K22 could not be confirmed.
- March count by Keep/research, march load per troop tier, and VIP-level gathering bonuses: not found.
- Free daily items/chests, monster drops and event RSS for farms: no specific sources found.
- Alliance resource tiles (alliance-owned RSS buildings) and their rates: not found.
- No reliable per-farm RSS/day benchmark that separates manual from bot play.

## Q3. Bots for multi-account farming: features, cloud vs emulator, pricing

### Takeaway
A crowded field of third-party TKR bots exists, most of them cloud-hosted (no PC or emulator needed). Pricing runs from about $1 per account per month (Fbots, self-run PC/emulator) to about $49/month for 3 accounts (Evony Auto). Farm-specific and multi-account services include:
- Fbots
- ESB TKR (Evony Smart Bot)
- BoostBot
- GnBots
- autofarmbots
- evonykingsreturnbot.com

Other bots focus on rallies or boss hunting rather than farming: iScope Auto, EvonAI, and Evony Auto's rally tools. **"Auto-transport to main" is advertised explicitly only as an ESB "Resources Transfer" feature**, with no detail found. All feature and safety claims are vendor marketing.

### Cited Findings
| Bot | Hosting | Pricing (as found) | Farm-relevant features found | Source |
|---|---|---|---|---|
| **Fbots** | PC program (own emulator) or shared server/cloud | From about $1/acct/mo (PC program); from about $4/acct (shared server) | Runs "farm" keeps that gather and stockpile 24/7 while the player runs the main; claims no bans recorded on its accounts but no guarantee | [fbots.org – Evony Bot](https://fbots.org/en/evony-bot) |
| **ESB TKR (Evony Smart Bot / ESB Cloud)** | Cloud (vendor servers), works with mobile/iPhone/Android | Intro: $5/mo first account + $3 each extra, plus a processing fee | Tile level and type selection; shared "Collective" tile queue (L15 only); "Resources Transfer" feature listed (no detail); Resource Gathering service; logs in hourly; recommends using it on farm accounts, not mains, and says ban risk always exists | [emulatorautomation.com – ESB Cloud](https://www.emulatorautomation.com/evony-cloud-bot); [ESB TKR – FAQ](https://www.evonysmartbot.com/p/faq.html); [ESB TKR – Farming Guide](https://www.evonysmartbot.com/2022/02/farming-guide.html); [ESB TKR – Other Services](https://www.evonysmartbot.com/p/other-services.html); [OwnedCore thread](https://www.ownedcore.com/forums/mmo/mobile-flash-game-hacks/994231-evony-kings-return-bot-auto-farm-unlimited-accounts-evony-tkr-bot.html) |
| **Evony Auto** | Cloud | Starter $49/mo for 3 Monarchs; Growth $99/mo for 10; Scale $149/mo for 25; 24h free trial for 1 Monarch | Rally auto-start and join, gathering, building, research, troop training | [evonyauto.com](https://evonyauto.com/) |
| **iScope Auto** | Cloud | Per-account price not captured; $30/mo "Rally Setter" add-on | Rally joining, gathering, peace-shield management, boss hunting | [auto.iscope.online](https://auto.iscope.online/) |
| **EvonAI** | Cloud | Solo $7.99/mo (1 acct), Squad $14.99, Fleet $26.99; 48h trial | Rally automation (farming features not confirmed) | [evonai.app](https://evonai.app/) |
| **GnBots (Evony TKR Bot / Evony Cloud Bot)** | Cloud option ("No Emulators or Downloads Required"); GnBots also sells an emulator-based product | Pricing not captured; free trial advertised | Auto-joins boss rallies, farms tiles | [GnBots – Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/); [GnBots – Evony TKR Bot](https://www.gnbots.com/shop/evony-tkr-bot/) |
| **BoostBot** | Per the comparison site, includes a managed "Farm-for-Me" service | "Farm-for-Me" about $12/acct/mo (per the comparison site); 6-month plan options exist | Managed farming | [boostbot.org – Evony Bot](https://boostbot.org/evony-kings-return-bot/); [bestmobilebots.com comparison 2026](https://bestmobilebots.com/evony-kings-return-bot/) (affiliate-style) |
| **autofarmbots.com** | Cloud ("Farm for Me") | "Farm for Me" from $8.00 per account per month (attributed via the search summary) | Auto-farm | [autofarmbots.com – Evony King's Return Bot](https://autofarmbots.com/evony-kings-return-bot/) |
| **evonykingsreturnbot.com** | Free Windows version; cloud tier | Free (limited); $25 premium; $80 cloud tier said to support up to 60 accounts (page about 449 days old, so roughly Aug 2025; prices may be outdated) | Auto-farm | [evonykingsreturnbot.com](https://evonykingsreturnbot.com/) |

- **Other bots on a comparison list.** An affiliate-style 2026 comparison site also lists LSS Bot, PrimeBot, ESB-TKR, Ragebot and MuBots for TKR. — [bestmobilebots.com – Best Evony TKR Bot Comparison 2026](https://bestmobilebots.com/evony-kings-return-bot/)
- **Scale claims.** Vendor pages claim "multi-account support for hundreds of farm accounts" and "many users manage 50+ farm accounts simultaneously." The search summary did not say which vendor made which claim; the pages in that result set were fbots.org, evonykingsreturnbot.com, autofarmbots.com, evonyauto.com, iScope, boostbot.org, GnBots and evonai.app. An OwnedCore thread advertises "Auto Farm Unlimited Accounts." — [OwnedCore – Evony TKR Bot thread](https://www.ownedcore.com/forums/mmo/mobile-flash-game-hacks/994231-evony-kings-return-bot-auto-farm-unlimited-accounts-evony-tkr-bot.html)
- **Session conflicts.** One vendor notes that Evony allows only one active session per account, so logging into the account pauses the bot (vendor not identified in the summary). ESB says its hourly logins can interrupt a player who is active, which is why it recommends running it on farms. — [ESB TKR – FAQ](https://www.evonysmartbot.com/p/faq.html)
- **Anti-detection claims.** One vendor claims human-like randomized delays and anti-detection settings (vendor not identified in the summary; marketing claim only).

### Inferences
- **Best fit for many-alt RSS farming.** Per-account cloud services designed around farms (ESB Cloud at $5 + $3 per extra account, Fbots shared server from about $4, autofarmbots from $8, BoostBot Farm-for-Me about $12) are far cheaper per alt than rally-oriented or tiered tools like Evony Auto (about $6–16 per Monarch per month). Fbots' $1/acct PC plan is cheapest but needs your own hardware and emulator per account.
- **ESB is the only bot with documented farm mechanics** (tile-level selection, a shared L15 tile queue, a listed "Resources Transfer" feature) and an explicit "use on farms, not main" stance. That makes it the most farm-specific option documented in these sources, though its guides date to Feb 2022.
- **Auto-transport to main is the weakest-documented feature** across vendors. Buyers should confirm it, and confirm that it respects Family Group, Embassy and daily caps, before choosing a bot.

### Gaps
- Per-account pricing for GnBots and iScope was not captured.
- Feature-level confirmation was not found for each vendor's auto-transport to main, auto daily-reward collection, auto building upgrades, auto-shield (only iScope lists shield management), and scheduling.
- Account-count limits per plan are known only for Evony Auto (3/10/25) and evonykingsreturnbot.com (60 on the cloud tier).
- No independent (non-vendor) reviews or uptime data were found.

## Q4. Player-reported results, complaints and ban risk

### Takeaway
No reliable player-reported RSS/day-per-farm figures with a bot were found. The only number is a ~2023 vendor YouTube claim of 4B RSS/day (28B/week), which is unverified and far above a community estimate of 300–400M/day for gathering. Ban evidence is thin: vendors either claim zero bans (Fbots) or concede the risk (ESB). Since the Family Group feature, resource transfers between linked accounts are officially not violations, but the sources do not say that permits bots.

### Cited Findings
- **Vendor bot claim.** "Farming BotBoss.4000 … How to get an extra free 28B RSS per Week" (4B/day) is a vendor promotional video about 1,124 days old (roughly Oct 2023). — [YouTube – Farming BotBoss.4000 for Evony TKR](https://www.youtube.com/watch?v=y4gfFQL_rz0) (**unverified, historical**)
- **Community benchmark.** Gathering can yield "upwards of three to four hundred million of resources per day." — [EvonyTKRGuide – Guide to Gathering Resources](https://www.evonytkrguide.com/guides/evony-tkr-guide-to-gathering-resources)
- **ESB on ban risk.** There is always a risk that Evony limits or bans bot accounts, and ESB recommends using bots on farm accounts, not mains. — [ESB TKR – FAQ](https://www.evonysmartbot.com/p/faq.html)
- **Fbots on ban risk.** It claims no bans have been recorded on its accounts, but does not guarantee it. — [fbots.org – Evony Bot](https://fbots.org/en/evony-bot)
- **Official stance on multi-account transfers.** Resource exchanges between Family Group members "regardless of the method, are not considered violations." This legitimizes multi-account RSS transfer, but only within a Family Group and only between same-alliance, same-server members. — [Top Games Inc. – Family Group Feature Announcement](https://info.topgamesinc.com/evony-family-group-feature-announcement/)
- **Player sentiment.** A YouTube community post says Family Group was "something Evony promised during the Dev Call following the coin …" (snippet truncated). It hints the feature responded to player complaints about penalties on multi-account transfers. — [YouTube community post on Family Group](https://www.youtube.com/post/UgkxJevlkucMi4fPEMlz_xn-VrgSa1D66lma)
- **Farms getting hit (historical).** A 2018 guide says to choose a secluded location and be ready to bubble (shield) both accounts if someone ports in. — [EvonyTKR.com – Setting up an Alt (2018)](https://evonytkr.com/2018/08/18/server-wars-setting-up-an-alt/) (**historical**)
- **Exposure on the main.** Transported RSS is unprotected on the receiving account. — [Top Games Inc. – Conditions for Sharing Resources](https://info.topgamesinc.com/docs/evonytkr/conditions-for-sharing-resources-within-a-family-group/)

### Inferences
- The Family Group announcement says transfers are not violations "regardless of the method," and its wording lists the previous methods (transportation, plundering, Royal Waybills). This implies such transfers were penalized before Family Group, which fits the user's concern about "bans focused on multi-account linking." Since then, the remaining risks are (a) using third-party automation itself and (b) transfers outside a Family Group.
- With no independent data, any per-farm RSS/day number with a bot should be presented as unverified. The vendor's 4B/day claim is about 10x the community gathering estimate.

### Gaps
- No Reddit (r/Evony, r/EvonyTKR) threads with bot results, ban reports or transport-cap complaints surfaced in searches.
- Evony's official Terms of Service or support statement on third-party bots/automation was not retrieved in this session.
- No documented ban waves targeting multi-account farms in 2025–2026 were found.
