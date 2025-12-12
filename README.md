# dennis-bot v0.4.0
A chaotic beginner-friendly Python bot with feelings, too many opinions and an unhealthy amount of confidence for someone who is one (1) year old.

This project is a learning space for Pythin fundamentals, structure and versioning.

Features (updated)
- Structured data folders (data/) for colors, names, robots, food, cities, jobs, and age-based responses
- Modular logic layer in modules/logic.py to handle categorization, variation mapping, and clean conversational flow
- Variation tables so Dennis understands different ways users say things (e.g., chat gpt, sfo, dev)
- Age buckets that interpret numerical input into categories like baby, teen, adult, ancient
- Termination conditions — certain answers make Dennis react dramatically before ending the chat
- Question bank with customized Dennis-flavoured prompts
- Clean conversational loop replaced with split handlers for each category
- Better fallback responses when Dennis doesn’t recognize an input

Planned Features
- State machine reactions
- API Integrations
- Holiday-based behaviour
- UI assets
- Emotion tracking and mood persistence

How to Run
1) Clone the repo.
2) Ensure you are using python 3.x
3) Run: main.py

This is a learning project. Expect chaos.


LICENSE

Copyright 2025 Naomi Anson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
