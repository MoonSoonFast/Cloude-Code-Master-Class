# Evony: The King's Return bots and monster soloing (solo hunting with marches)

*How this was researched (read before using these notes):* WebFetch was blocked in this session for every vendor domain tried (emulatorautomation.com, gnbots.com, evonyauto.com, bestmobilebots.com all failed with "host outside allowed network domains"). Every claim below therefore comes from **search-result snippets and summaries** of the cited pages, not full page reads. Vendor claims are marketing and were not tested. Dates are given where the page or search result showed one; "date unknown" means the snippet did not show one. Research date: 2026-11-10.

---

## Q1. Which bots advertise monster soloing / hunting, and which monster types and levels do they support?

### Takeaway
At least nine third-party TKR bots mention monster hunting. Only a few describe a real **solo** mode with per-monster settings: ESB Cloud ("soloable lists", presets, chaining, stamina rules), Ragebot TKR ("Solo Bosses" plus a per-boss March Designer, not cloud), the older desktop ESB-TKR "Monster Kill Mode" (regular monsters only, not bosses), and iScope's preset system with a monster filter. GN Bots, Evony Auto and fbots say "hunt/attack monsters" but give no detail on monster types or levels. EvonAI is built around rallies and does not advertise soloing.

### Cited Findings
**Cloud-hosted bots**
- **ESB Cloud** (Emulator Automation, cloud version of ESB, runs on the developer's servers): its "Auto Setter can kill bosses and monsters with named presets, troop tiers, soloable lists, chaining and stamina rules." It is the most solo-specific feature list found. The snippet did not say how chaining or the stamina rules work. Date unknown, probably 2026. — [ESB Cloud page](https://www.emulatorautomation.com/evony-cloud-bot)
- The same vendor's 2026 blog says Evony bots can "start rallies on boss monsters yourself (an 'auto setter'), or solo the bosses your marches can handle." — [ESB Blog: What is an Evony bot? (2026)](https://www.emulatorautomation.com/Blog/what-is-an-evony-bot)
- **GN Bots Evony Cloud Bot** (no emulator or download): advertises that it can "automatically hunt monsters, join boss rallies, use stamina, and collect rewards", "recruit powerful generals, hunt world monsters, manage marches, and keep your armies active", start and join boss rallies automatically, and watch for attacks to shield. No monster levels or types named in the snippets. Date unknown. — [GN Bots Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/); [GN Bots TKR bot page](https://www.gnbots.com/evony-kings-return-bot/)
- **Evony Auto** (cloud, "no PC, emulator or install"): "attacks monsters, builds, researches, trains troops and claims your dailies" across Monarchs, plus Rally Auto-Start and Rally Auto-Join 24/7 and "scout missions and map scans". No detail on monster levels or march presets. Date unknown. — [Evony Auto](https://evonyauto.com/)
- **EvonAI** (cloud): "auto-joins alliance rallies, leads your own boss rallies, scouts the whole map, and tops up stamina, 24/7 in the cloud." It also offers a "full, always-fresh map of every boss on your server with exact coordinates" and Discord alerts for boss spawns. "Solo" is the name of its single **pricing plan**, not a solo-hunting feature. The page does not say it solos monsters. Date unknown. — [EvonAI](https://evonai.app/)
- **iScope Auto / iScope Recon**: iScope Auto lists "auto rally joining with monster filter and boss monster hunting". iScope Recon is a map-intelligence and boss-scanner product. The **Rally Setter** add-on uses presets that are "a full march recipe with a general, an assistant general, a troop composition, and an optional monster filter". The presets "fire round-robin: preset 1 kills the first monster, and when that march returns, preset 2 targets the next". You can "dedicate one preset purely to event monsters and another to high-level world bosses". The product is named for rallies, so the snippets do not make clear whether these are solo hits or rally starts. The add-on is listed at "$30/month extra". Blog dated 2026. — [iScope Rally Setter blog (2026)](https://www.iscope.online/blog/evony-rally-setter); [iScope Auto](https://auto.iscope.online/); [iScope Auto compare page](https://auto.iscope.online/compare/iscout); [iScope Recon](https://www.iscope.online/)
- **fbots.org**: "24/7 auto-farming". Says "monster hunts, enemy sieges and city defence are scheduled". No detail on marches or targets. Date unknown. — [fbots.org Evony bot](https://fbots.org/en/evony-bot)

**Desktop/emulator bots (not cloud)**
- **ESB-TKR** (Evony Smart Bot, desktop/emulator): "Monster Attacking: Solo attack regular monsters, **not bosses**, on the map." Its "Monster Kill Mode lets you solo monsters (not bosses) on the map, including dark knights." The bot needs the map zoomed out, and the game must be full screen or zooming fails. Guides are from 2021–2022, so they are **historical**. — [ESB-TKR How to use (Jan 2022)](https://www.evonysmartbot.com/2022/01/part-2-how-to-use-evony-smart-bot.html); [ESB Monster Kill Guide (Feb 2022)](https://www.evonysmartbot.com/2022/02/monster-kill-guide.html); [ESB Monster Kill Guide, blogspot (Oct 2021)](https://evonysmartbot.blogspot.com/2021/10/monster-kill-guide.html)
- ESB-TKR also has a **Boss Finder** mode and an **Auto Setter** mode for bosses. A vendor YouTube video says it can "set bosses as fast as 20 seconds per boss (Proper equipment and settings required)". The video was about 953 days old when searched, so roughly early 2024. — [ESB Auto Setter Guide (Feb 2022)](https://www.evonysmartbot.com/2022/02/auto-setter-guide.html); [YouTube: Auto Set Bosses Faster with Evony Smart Bot](https://www.youtube.com/watch?v=QqnR4aICc74); [YouTube: Automatically Attack and Find Bosses using ESB](https://www.youtube.com/watch?v=J3IOhJ13pgo)
- **Ragebot TKR** (rage.systems, emulator-based): its Start Rallies routine uses a **March Designer** "where you set up battle marches for each boss". A **Solo Bosses** setting "lets the bot kill certain monsters alone instead of rallying them, such as low-level monsters". The routine pauses when no march can kill a boss and restarts when one is free. The manual warns that "most servers dislike players soloing large bosses." Manual date unknown. — [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html)
- A 2026 comparison site says Ragebot TKR needs a "540x960 portrait resolution" and, like ESB-TKR, "lacks cloud hosting". It names ESB-TKR and Ragebot TKR as the Evony specialists noted for rally automation. — [BestMobileBots TKR bot comparison (2026)](https://bestmobilebots.com/evony-kings-return-bot/)
- **Pixelbotter** (OwnedCore thread, roughly 3.8 years old, so about early 2023, **historical**): "Auto Hunt monsters (all or custom monsters)", "Auto join rally (all or custom monsters)", multi-instance, "100% Image based & 100% client sided", runs on Bluestacks over ADB. No current product page found. — [OwnedCore Pixelbotter thread](https://www.ownedcore.com/forums/mmo/mobile-flash-game-hacks/982118-evony-auto-rally-bot-evony-tkr-auto-boss-hunt-monster-hunt-set-rallies-alliance-informer.html)
- **evony-helper.com "mobile bot"** (July 2022, **historical**): rally-boss bot priced at "1 account = 6 USD (rally boss) per month", with boss selection. — [evony-helper mobile bot](http://www.evony-helper.com/2022/07/mobile-bot.html)
- **Boss Radar + Evonex**: Boss Radar's scanner covers "bosses, collectables, resource tiles, sub-cities and event targets". Evonex sends the rallies. This is a scanning and rally tool, not soloing. — [Boss Radar](https://bossradar.app/)

**Monster categories the bots may target** (game facts, for context)
- TKR has normal monsters (a fan-wiki reward table runs from Lv1–Lv9 normal monsters up to a Lv19 Barbarian) and named bosses. Normal monsters are attacked solo, while bosses are usually rallied. — [Fandom: Normal Monsters](https://evony-the-kings-return.fandom.com/wiki/Normal_Monsters); [Fandom: Boss Monsters](https://evony-the-kings-return.fandom.com/wiki/Boss_Monsters)
- Named bosses in current guides include Zombie (L1), Manticore, Kamaitachi, Cerberus (Junior/Medium/Legendary), Hydra, Ymir, Witch, Warlord, Pan, Phoenix, Kraken, Azazel and Typhon. — [EvonyTKRGuide Zombie](https://www.evonytkrguide.com/bosses/zombie); [EvonyTKRGuide Manticore](https://www.evonytkrguide.com/bosses/manticore); [EvonyTKRGuide Kamaitachi](https://www.evonytkrguide.com/bosses/kamaitachi); [Evony Guide Wiki boss power list](https://evonyguidewiki.com/en/boss-power-list-en/); [Theria Games: Bosses](https://theriagames.com/guide/bosses/)

### Inferences
- If "soloing" means the bot picks individual monsters or bosses and sends one march per kill, the strongest documented options are **ESB Cloud** (cloud; "soloable lists" and "chaining") and **Ragebot TKR** (not cloud; per-boss March Designer plus Solo Bosses). **iScope** is close behind (per-preset monster filter, round-robin presets), but it may be rally-oriented. ESB-TKR desktop solos only regular monsters, not bosses.
- GN Bots, Evony Auto and fbots advertise hunting, but nothing public found shows granular controls (monster level ranges, a troop preset per monster). Their solo capability may be basic or simply undocumented publicly.
- EvonAI should not be counted as a soloing bot. Its pitch is rally join/lead, boss mapping and stamina top-up.

### Gaps
- No vendor snippet listed the exact monster types or level ranges each bot supports for solo hits (e.g., whether ESB Cloud can solo Cerberus, Pan or Ymir, or only low-level bosses). Full pages could not be fetched.
- "Bloody Marry" and any 2025–2026 event-only monsters: no source found on bot support.
- Whether iScope Rally Setter "kills" are solo attacks or rally starts is ambiguous in the snippets.
- No current (2025–2026) Pixelbotter or evony-helper pages were found. These may be defunct.
- Other bot sites appeared in results without monster-feature details: boostbot.org, autofarmbots.com, evonykingsreturnbot.com, evonylife.com. Unknown.

---

## Q2. How do the bots make soloing fast (marches, stamina, healing, presets, scanning, re-march, chaining)?

### Takeaway
The documented speed levers are: automatic stamina use (ESB-TKR up to 9,999; ESB Cloud "stamina rules"; EvonAI stamina top-up; GN Bots "use stamina"); presets fired round-robin as marches return (iScope); chaining (ESB Cloud, details unknown); map scanning and boss maps (EvonAI, iScope Recon, Boss Radar, Evony Auto); a healing routine (Ragebot); and auto-suspend when no march can win (Ragebot). No vendor publishes march-count logic, re-march latency or search-radius specs.

### Cited Findings
- **Stamina use:** ESB-TKR's Monster Kill Mode has a "Consume Stamina" option that "will automatically consume stamina for you up to 9,999" (2022). — [ESB Monster Kill Guide (Feb 2022)](https://www.evonysmartbot.com/2022/02/monster-kill-guide.html)
- ESB Cloud lists "stamina rules" alongside presets, troop tiers, soloable lists and chaining. — [ESB Cloud page](https://www.emulatorautomation.com/evony-cloud-bot)
- EvonAI "tops up stamina" 24/7. — [EvonAI](https://evonai.app/)
- GN Bots lists "use stamina" among its automatic actions. — [GN Bots Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/)
- **Presets and re-march:** iScope presets each carry general, assistant general, troop composition and an optional monster-group filter. They "fire round-robin: preset 1 kills the first monster, and when that march returns, preset 2 targets the next." — [iScope Rally Setter blog (2026)](https://www.iscope.online/blog/evony-rally-setter)
- **Per-target march design:** Ragebot's March Designer sets up battle marches for each boss. The routine "is suspended when no march can kill a boss" and re-enables once one is free. — [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html)
- **Healing:** Ragebot's Healing routine has a "Heal Threshold" (hours of healing to queue, e.g. a 6-hour setting picks enough troops for 6 hours of healing), a "Help Offset" for alliance-help time, and "Heal All" and "Speed Up" options. — [Ragebot manual: Healing](https://rage.systems/manual/healing.html)
- **Map scanning:** EvonAI keeps a "full, always-fresh map of every boss on your server with exact coordinates". — [EvonAI](https://evonai.app/)
- Evony Auto advertises "scout missions and map scans". — [Evony Auto](https://evonyauto.com/)
- Boss Radar's scanner covers bosses, event targets and more. — [Boss Radar](https://bossradar.app/)
- iScope Recon is a "map intelligence" platform. — [iScope Recon](https://www.iscope.online/)
- ESB-TKR (desktop) scans visually and needs the map zoomed out at full screen. — [ESB Monster Kill Guide (Oct 2021)](https://evonysmartbot.blogspot.com/2021/10/monster-kill-guide.html)
- **Speed claim:** an ESB video says the Auto Setter can "set bosses as fast as 20 seconds per boss (Proper equipment and settings required)". This is a vendor claim from about early 2024 and describes rally setting, not solo kills. — [YouTube: Auto Set Bosses Faster with ESB](https://www.youtube.com/watch?v=QqnR4aICc74)
- **Multi-account:** Evony Auto runs across multiple "Monarchs". Pixelbotter advertised "Multi Instance". — [Evony Auto](https://evonyauto.com/); [OwnedCore Pixelbotter thread](https://www.ownedcore.com/forums/mmo/mobile-flash-game-hacks/982118-evony-auto-rally-bot-evony-tkr-auto-boss-hunt-monster-hunt-set-rallies-alliance-informer.html)

### Inferences
- Cloud bots that read map data (EvonAI, iScope Recon, Evony Auto "map scans") probably find targets faster than the screen-scanning desktop approach (ESB-TKR zooming the map). That is an inference from how each product describes itself, not a measured comparison.
- Because stamina is the binding constraint (see Q5), the most important "fast" feature is likely automatic stamina-item use without stalls. ESB (both versions), EvonAI and GN Bots mention it. Healing automation (documented in detail only for Ragebot) matters most when the bot under-sizes marches.
- "Chaining" in ESB Cloud probably means sending a march to the next target as soon as one returns or completes, similar to iScope's round-robin. This is unconfirmed.

### Gaps
- No bot documents how many simultaneous solo marches it runs, whether it fills all march slots, or how it handles slot limits.
- No vendor spec on search radius, re-march latency, or whether it uses march-speed items.
- No source on bots using the "Monster Hunting" events or monster-specific general skills automatically. iScope presets name a general per preset, but that is manual configuration.
- ESB Cloud's "chaining" and "stamina rules" are undefined in available snippets.

---

## Q3. Do any bots calculate optimal troop composition (minimum troops to one-shot, zero-wound, layering), or support "speed solo" setups?

### Takeaway
No bot was found that **computes** an optimal or minimum troop count per monster. Bots rely on user-built presets (ESB Cloud "named presets / troop tiers", iScope preset troop composition, Ragebot March Designer). The math lives in community tools, mainly the Evony Guide Wiki Boss Battle Simulator, which gives zero-wound troop counts that users then put into bot presets.

### Cited Findings
- ESB Cloud supports "named presets, troop tiers" and "soloable lists", meaning the user defines which targets are soloable with which preset. — [ESB Cloud page](https://www.emulatorautomation.com/evony-cloud-bot)
- iScope presets include a "troop composition" chosen by the user. — [iScope Rally Setter blog (2026)](https://www.iscope.online/blog/evony-rally-setter)
- Ragebot's March Designer is where "you set up battle marches for each boss". The bot pauses when "no march can kill a boss". This suggests some win-check, but the snippet does not say whether it calculates or the user specifies. — [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html)
- **Community calculator:** the Evony Guide Wiki **Boss Battle Simulator** estimates "win/loss and wounded simulation, RSS balance, battle log, attack buff calculation". Its zero-wound figure comes from monster HP divided by damage per soldier, which depends on attack and monster defense. Wiki users report that simulator results do not always match real battles. — [Evony Guide Wiki Boss Battle Simulator](https://evonyguidewiki.com/en/calculator-number-of-troops-to-kill-boss-en/); [How Many Troops need to Defeat Boss?](https://evonyguidewiki.com/en/how-many-troops-defeat-boss-en/)
- Example thresholds: Junior Hydra needs "t12 Cavalry 500,000+ / Zero wounds at 1,000,000". Cerberus 1 needs "t11 Cavalry 250,000+ / Zero wounds at t11 Cavalry 450,000". These pages were about 1–1.5 years old when searched. — [How to kill Hydra](https://evonyguidewiki.com/en/how-to-kill-hydra-en/); [How to kill Cerberus](https://evonyguidewiki.com/en/how-to-kill-cerberus-en/)
- For zero wounds, "a general with more 'attack' and 'march size' is the better pick". Stack the monster-specific mounted attack skillbook with the general mounted attack skillbook. — [Evony Guide Wiki: Best Boss General / Monster Hunter](https://evonyguidewiki.com/en/best-boss-monster-general-en/)
- **Layering:** sending low-tier troops with high-tier ones "can end the battle early" in World Boss fights. A TKR player guide warns that hitting with lower-level troops first "takes up hospital space that could be reserved for your tougher troops" and advises picking "a monster you can kill, or you will wind up with lots of healing anyway". — [One Chilled Gamer World Boss Guide](https://onechilledgamer.com/evony-world-boss-guide/); [Evony TKR Player's Guide: Monarch Events](https://evonyplayersguide.blogspot.com/p/beginner-tip-6-monarch-events.html)
- Most layering guides are PvP-focused. They note that every added layer "takes up precious space in your march". — [LDShop: PvP guide troop layering](https://www.ldshop.gg/blog/evony-the-kings-return/pvp-guide-troop-layering.html)
- **Event-specific "1-troop" setups:** a December 2025 Monster Hunt rallies guide says to "Set troop count to one troop only" and that "each preset must use different copies of both generals, each at the correct levels". This is for an event rally mechanic, not standard solo kills. — [Clashiverse: Evony Monster Hunt Rallies Guide (Dec 2025)](https://clashiverse.com/evony-monster-hunt-rallies-guide/)

### Inferences
- A "speed solo" setup in practice means presets sized just above the win threshold (or at zero-wound size to avoid healing downtime), using mounted troops and a monster-attack general. The user does this sizing, probably with the Guide Wiki simulator. Bots only execute it.
- A bot that under-sizes marches causes wounded troops and hospital load. One that over-sizes wastes march capacity and slows parallel kills. Without built-in calculators, preset quality depends on the user.

### Gaps
- No evidence found of any TKR bot with a built-in troop calculator or automatic minimum-troop sizing. This could exist behind paywalls or in Discord-only docs that could not be checked.
- Whether Ragebot's "no march can kill a boss" check uses a damage model or a user-set rule is unknown.

---

## Q4. Measured or player-reported kill rates, and complaints (wrong troops, losses, getting stuck)?

### Takeaway
No measured or player-reported kills-per-hour or kills-per-day figures for any TKR bot were found. The only speed figure is a vendor claim ("20 seconds per boss" to set rallies, ESB). Public complaints found concern botting in general (Trustpilot), not specific bot failures. No bot-specific reports of wrong troops or stuck marches surfaced.

### Cited Findings
- ESB vendor video: the Auto Setter can "set bosses as fast as 20 seconds per boss (Proper equipment and settings required)". This is rally setting, not a solo kill rate, from about early 2024. — [YouTube: Auto Set Bosses Faster with ESB](https://www.youtube.com/watch?v=QqnR4aICc74)
- Trustpilot reviews of Evony (the game, not bots) complain that "monsters have increased power, spawning of monsters has slowed down". Reviewers also report "mass botting with almost 100 bot accounts" and say enforcement is lax. Reviews are unverified and of mixed dates. — [Trustpilot: Evony reviews](https://www.trustpilot.com/review/www.evony.com); [Trustpilot page 3](https://www.trustpilot.com/review/www.evony.com?page=3)
- An aggregator lists Evony at 1.7/5 from 125 customers (2026). — [SmartCustomer: Evony reviews](https://www.smartcustomer.com/reviews/evony.com)
- Ragebot warns that "most servers dislike players soloing large bosses". This is a social and political risk of bot soloing. — [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html)
- Guide Wiki users report simulator results that don't always match real battles, a risk if bot presets are sized from the simulator. — [Evony Guide Wiki Boss Battle Simulator](https://evonyguidewiki.com/en/calculator-number-of-troops-to-kill-boss-en/)
- Searches of Reddit for "evony bot hunting monsters lost troops" returned no Evony-relevant Reddit threads. — (search returned only unrelated results; no URL to cite)

### Inferences
- The question "which bot solos fastest" **cannot be answered from public evidence**. No independent benchmark or player-reported throughput exists in what was searchable. Any "fastest" ranking would be speculation.
- The "slowed monster spawns" complaint, if accurate, means map density can cap solo throughput no matter which bot is used.

### Gaps
- No Reddit (r/Evony, r/EvonyTKR), Discord or YouTube comment evidence of bot kill rates was retrieved. Reddit did not surface in search, and pages could not be fetched.
- No Trustpilot pages found for the bot vendors themselves (ESB, GN Bots, Evony Auto, EvonAI, iScope, Ragebot).
- No reports found of bots sending wrong troops, losing troops or getting stuck. This does not mean such issues don't happen; they just weren't surfaced.

---

## Q5. What in-game mechanics determine solo speed (what a bot can and can't optimize)?

### Takeaway
Solo throughput is limited mainly by **stamina**: about 1 point per 240 seconds (about 15/hour, about 360/day), with natural regen capped at 100 and a daily reset to 100. Monster costs are 6 (normal, per fan wiki) to 15–50 stamina (bosses). Next come **march slots** (max 6: four research items plus a VIP 5 slot), **march size** (keep level and buffs), **troop/general strength** (mounted plus monster-attack generals), and **wounds/healing**. A bot can use stamina items, keep stamina below the cap, fill slots, re-march instantly and auto-heal. It cannot raise base regen, slot count, monster spawn density or troop strength.

### Cited Findings
**Stamina**
- Stamina regenerates at about one point every 240 seconds, lowered by buffs. That is about 360 stamina per day if you keep spending it. — [LDShop: How to Get More Stamina](https://www.ldshop.gg/blog/evony-the-king-s-return/get-stamina.html); [Theria Games Stamina Guide](https://theriagames.com/guide/evony-stamina-guide/)
- Recovery speed depends on "monarch talent and vip level". The regeneration talent is at Monarch Level 18. — [Fandom: Stamina](https://evony-the-kings-return.fandom.com/f/p/4400000000000023178); [EvonyGuru Stamina Guide](https://www.evonyguru.com/monarch/stamina.html)
- Stamina regenerates only while below 100. Several guides say stamina is restored to 100 at the daily server reset. — [EvonyGuru Stamina Guide](https://www.evonyguru.com/monarch/stamina.html); [Theria Games Stamina Guide](https://theriagames.com/guide/evony-stamina-guide/)
- **Costs:** Zombie (L1, 36,500 power) costs 15 stamina; Manticore (2.2M power) 20; Kamaitachi (89.4M power) 35. — [EvonyTKRGuide Zombie](https://www.evonytkrguide.com/bosses/zombie); [Manticore](https://www.evonytkrguide.com/bosses/manticore); [Kamaitachi](https://www.evonytkrguide.com/bosses/kamaitachi)
- Boss levels 1–7 cost 15 or 20 stamina. — [One Chilled Gamer Boss Guide](https://onechilledgamer.com/evony-boss-monster-guide/)
- Higher bosses cost 20–50 (e.g., Legendary Cerberus Lv4 = 40, Typhon Lv17 = 50); Medium Cerberus = 30. — [Evony Guide Wiki boss power list](https://evonyguidewiki.com/en/boss-power-list-en/)
- Normal monsters cost "6 stamina points" per march, per a fan wiki. — [Fandom: Normal Monsters](https://evony-the-kings-return.fandom.com/wiki/Normal_Monsters)
- **Conflicting:** a search summary quoted "normal monsters: 20 stamina" from an unidentified page, and another guide says normal monsters "consume much less stamina" than bosses. Treat the normal-monster cost as uncertain. — [Evony Guide Wiki: Creating Wounded Troops](https://evonyguidewiki.com/en/make-wounded-as-you-need-en/)
- **Reward per stamina** (useful for choosing targets): Ymir L3 is about 266,667 total resources per stamina; Azazel about 400K, Kraken about 320K, Ymir 6 about 290K. Cerberus L3 gives the most speed-ups per stamina, followed by Pan L6 and Pan L5. Figures are from two guides (snippet attribution between them not confirmed); the newest ranking is about 11 months old. — [Theria Games: Bosses](https://theriagames.com/guide/bosses/); [EvonyTKRGuide: Best Boss Rewards](https://www.evonytkrguide.com/guides/evony-tkr-guide-to-best-boss-rewards-rss-resources-speed-ups-comparison)

**March slots and size**
- March slots start at 1 and max out at 6. Four research items add one each: Formation (Academy Lv6), Advanced Dispatch, Super Advanced Dispatch, and Legion Expansion (Academy Lv35). VIP 5 with an active VIP adds +1, and no more at higher VIP. — [Theria Games: March Slots Guide](https://theriagames.com/guide/march-slots-guide-evony/); [Evony Guide Wiki: How to get more March Slot](https://evonyguidewiki.com/en/how-to-get-more-march-slot-en/)
- Keep level governs **march size**, not slot count. Examples: about 518,200 troops per march at K26 and about 4,527,500 at K40, both under assumed buffs. — [Evony Guide Wiki: Maximum March Size by keep level](https://evonyguidewiki.com/en/march-size-per-level-en/)
- One guide assumes 5 marches at K25. — [Evony Builds: Layered PvP Marches](https://evonybuilds.com/guide-to-layered-pvp-marches-total-troops-by-keep-level/)

**Combat / wounds**
- Monster battles are turn-based and the player strikes first. If the monster is not killed in the first turn, it attacks back. Bosses count as Ground units, so Mounted troops are best. — [Evony TKR Player's Guide: Battle Mechanics](https://evonyplayersguide.blogspot.com/p/think-rockpaperscissors.html); [Evony Guide Wiki: Battle Mechanics (Monster, Boss)](https://evonyguidewiki.com/en/monster-battle-mechanics-en/)
- Ranged or Ground troops need "more than twice as many troops as Mounted" for monsters. Siege should not be used unless the march is big enough to "ensure ZERO wounds". — [Evony Guide Wiki: Troop Type Guide](https://evonyguidewiki.com/?p=3714)
- Wounds are capped at about 10% in a monster battle, and normal monsters "can only wound 5%". Ragebot notes that a failed boss attack wounds at most 10%. In normal monster fights the wound *rate* drops stepwise as troop count rises. — [Evony Guide Wiki: Creating Wounded Troops](https://evonyguidewiki.com/en/make-wounded-as-you-need-en/); [Evony Guide Wiki: Battle Mechanics](https://evonyguidewiki.com/en/monster-battle-mechanics-en/); [Ragebot manual: Healing](https://rage.systems/manual/healing.html)
- World Bosses: "wounded troops do not occur". — [Evony Guide Wiki: World Boss](https://evonyguidewiki.com/en/world-boss-en/)

**Generals / buffs**
- Julius Caesar with his skin: "+165% mounted attack against monsters" and "+15% double item drop rate". This 2026 tier list comes from a game-item seller's blog. — [LDShop Generals Tier List 2026](https://www.ldshop.gg/blog/tier-list/evony-the-king-s-return-generals-tier-list.html)
- "For monster hunting, attack is the most important thing, so Hannibal." The page was updated about 17 days before 2026-11-10. — [Evony Guide Wiki: Best Mounted General](https://evonyguidewiki.com/en/best-mounted-general-en/)
- Key skillbooks: "Mounted Troop Attack Against Monster +45%" and "Mounted Troop Attack +25%" (Lv4). Theodora with a Luck book suits players who want drops. — [Evony Guide Wiki: Best Boss General / Monster Hunter](https://evonyguidewiki.com/en/best-boss-monster-general-en/); [One Chilled Gamer: Monster General Tier List](https://onechilledgamer.com/evony-monster-general-tier-list/)

### Inferences
- **Back-of-envelope throughput** (my arithmetic from the cited figures; costs uncertain): at about 15 stamina/hour plus the daily reset of 100, a bot running 24/7 on natural regen alone has roughly 460 stamina/day. That covers about 75 normal-monster hits at 6 stamina, or about 23–30 low bosses at 15–20 stamina, or about 9–15 high bosses at 30–50. Above that, kills scale only with **stamina items** (ESB's "up to 9,999" option) or regen buffs (VIP, Monarch talent).
- With stamina as the bottleneck, march-slot count and march speed matter only when the bot spends stamina items in bulk. At natural regen, even 1–2 marches can spend all the stamina available.
- What a bot **can** optimize: never letting stamina sit at 100, using stamina items per user rules, choosing targets by reward per stamina, filling all slots, re-marching immediately, sizing presets to avoid wounds, and auto-healing. What it **cannot** change: base regen, max slots (6), march size (keep level and buffs), monster spawn density and respawn, and general and troop strength.

### Gaps
- Exact current stamina costs for normal monsters (6 vs higher), Witch, Warlord, Kraken, Hydra and Pan were not confirmed from a current primary source.
- No source found on monster respawn timers or map density per server.
- No source found on march-speed buffs specific to monster marches.

---

## Q6. Overall: which bot(s), especially cloud ones, solo monsters fastest and best?

### Takeaway
On public evidence, **ESB Cloud** has the most solo-specific cloud feature set: named presets, troop tiers, soloable lists, chaining and stamina rules. **iScope** (presets with general, assistant, troops and monster filter, fired round-robin; $30/mo add-on) is the next most detailed, but may be rally-oriented. **Ragebot TKR** has strong solo and heal controls but no cloud hosting. GN Bots and Evony Auto advertise hunting without detail. EvonAI is rally-focused. **No independent data ranks any of them on speed**, so "fastest" is unproven.

### Cited Findings
- ESB Cloud: "kill bosses and monsters with named presets, troop tiers, soloable lists, chaining and stamina rules." — [ESB Cloud page](https://www.emulatorautomation.com/evony-cloud-bot)
- iScope presets: general, assistant general, troop composition and optional monster filter, round-robin as marches return. Rally Setter is a "$30/month extra" add-on. — [iScope Rally Setter blog (2026)](https://www.iscope.online/blog/evony-rally-setter); [iScope Auto compare page](https://auto.iscope.online/compare/iscout)
- Ragebot: Solo Bosses plus a per-boss March Designer, auto-suspend when no march can win, and a detailed Healing routine. No cloud hosting, and it needs a 540x960 portrait resolution. — [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html); [Ragebot manual: Healing](https://rage.systems/manual/healing.html); [BestMobileBots comparison (2026)](https://bestmobilebots.com/evony-kings-return-bot/)
- ESB-TKR (desktop, 2022): solos regular monsters only, with auto stamina use up to 9,999. — [ESB Monster Kill Guide (Feb 2022)](https://www.evonysmartbot.com/2022/02/monster-kill-guide.html)
- GN Bots: "automatically hunt monsters ... use stamina", "manage marches". — [GN Bots Evony Cloud Bot](https://www.gnbots.com/auto/evony-cloud-bot/)
- Evony Auto: "attacks monsters", map scans, multi-Monarch. — [Evony Auto](https://evonyauto.com/)
- EvonAI: rally join/lead, boss map, stamina top-up. No solo feature stated. — [EvonAI](https://evonai.app/)

### Inferences
- For a reader who wants a **cloud** bot that solos monsters with control over which targets and which troops, ESB Cloud is the best-documented match. iScope is an alternative if its presets do solo hits. Both rest on vendor claims only.
- Since stamina caps throughput (Q5), the "fastest" bot in practice is the one that reliably spends stamina items under user rules, never stalls, and avoids wounds. Public material cannot separate the vendors on those points.
- Bot use carries account risk. Trustpilot reviewers say mass botting is "against their TOS", and Ragebot itself warns that servers dislike solo boss sniping. — [Trustpilot: Evony reviews](https://www.trustpilot.com/review/www.evony.com); [Ragebot manual: Start Rallies](https://rage.systems/manual/startrallies.html)

### Gaps
- No head-to-head tests, benchmarks or player throughput reports. "Fastest" remains unknown.
- Current pricing for ESB Cloud, GN Bots, Evony Auto and EvonAI for monster features was not captured (pages not fetchable).
- To close these gaps, a future pass should allow network access to emulatorautomation.com, gnbots.com, evonyauto.com, evonai.app, iscope.online, rage.systems, bestmobilebots.com and reddit.com, then read full pages, changelogs and r/Evony threads.
