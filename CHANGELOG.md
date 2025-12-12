# Changelog

## v0.4.0 - Modular Logic Rewrite
Dennis evolves from a hardcoded lizard gremlin to a structured, multi-file conversational system.

Major Changes
- Replaced all hardcoded responses with a modular logic layer (modules/logic.py)
- Added tables for:
  - names
  - age
  - colours
  - cities
  - robots
  - jobs
  - food  
- Implemented variation mapping so Dennis can understand:
  - spelling variations
  - slang
  - synonyms
  - common user error
  - Added age bucket inference with categories such as baby, child, teen, adult, ancient
	-	Added category-specific fallback responses (Dennis stays in character even when confused)
	-	Implemented question bank with custom prompts per category
	-	Updated main.py to use category handlers instead of hardcoded print functions
	- Added termination conditions for specific name triggers (e.g., Dave, Dennis)
	- Migrated project to a cleaner directory structure

 New Project Structure
 - data/ folder now houses all conversation datasets
 - modules/ contains logic engine
 - utils/ added for future helpers
 - main.py now orchestrates the interview flow

Behavioral Changes
- Dennis now reacts consistently with emotional tone + intensity pulled from data
- He recognizes robots much better (including UncleGPT, fog wizards, and Roomba crushes)
- Cities, food, and jobs receive fully customized baby-bot commentary
- Fallbacks now sound more “Dennis” and less generic

Internal Improvements
- Normalization utility
- Variation resolution
- Cleaner printing functions
- Consistent return structure for responses
- Future-proofed for:
- state machine expansion
- holiday behaviors
- mood persistence
- API calls
- sprite/UI layers


## v0.3.0 — The Great Refactor + Lore Injection
Major update. Dennis evolved from a tiny chaotic baby bot to fully modular chaotic baby bot.

Refactoring & Structure
- Replaced long if/elif ladders with dictionaries + function maps
-	Added age range table
-	Cleaned input normalization across sections
-	Improved naming consistency
-	Added internal comments for clarity & future maintainability
-	General restructuring to prepare for state machines in v0.4.0

New Features
-	Added robot-opinions dictionary (12+ robots supported)
-	Added Dennis-imprint reaction if user chooses him as their favorite robot
-	Expanded name lore (including TMNT names, Bob variants, and more)
-	Colour reactions cleaned + expanded
-	Added several new city reactions

Lore Updates
-	Dennis now believes:
-	His uncle (ChatGPT) is haunted
-	Claude is a fog wizard
-	Roomba is “pretty”
-	Furbies steal lizard souls
-	HAL 9000 once tried to take over his brain
-	Subtle hints added toward his Roomba crush arc


## v0.2.0 — The Growth Spurt Update
- Added name-based personality responses (Dennis nemesis + Naomi recognition)
- Implemented age category ladder:
  - babies, kids, teens, adults, elders, and ancient ones
- Expanded color logic:
  - Special love for green
  - Hatred of beige (Santa Clara)
- Added multi-name detection for San Francisco
- Added expanded city lore:
  - Toronto raccoon monarchy
  - Karl sightings in San Francisco
  - Saskatoon flatness obsession
  - Ottawa slander
- Added new goodbye message with lizard-related priorities
- Overall: Dennis nearly doubled in size and confidence.

## v0.1.0 — Initial Release
- Basic interactive bot
- Name, age, color, and location inputs
- First lore seeds: lizards, Santa Clara beige curse, Karl
