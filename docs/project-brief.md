#Project Brief

**Status:** Draft v0.1 (Nov 2026). Revised after student interviews! 

## Problem

Most planners, if not all treat every equal and look at things from one perspective. Students often come home from class or practice exhausted, and a schedule that they ignore due to their exhaustion. Students end up with schedules that look reasonable on paper but later fall apart in practice. 

## Solution/Idea

Luma is a planning app that schedules tasks around a student's 'energy levels'. Users rate their energy from 1 to 5 once or twice a day. Luma, after time learns when the user tends to be drained, then places harder tasks in higher-energy times and easier/lighter tasks in lower-energy times. Each placement comes with an explanation. 

## Audience

High school students and undergrad students who struggle with deadlines, assignments, clubs, activities, etc. Early testing will be focused on high school students. 

## Principles

- **Transparent:** every suggestion has a reason the user can read.
- **User-reported:** Luma only uses the energy ratings users enter
  themselves. It does not guess mood from sensors or text.
- **A planning aid, not a health tool:** it does not diagnose or
  treat anything.
- **Calm and accessible:** the design should feel low-pressure and be
  usable by everyone.

## Research question

Is energy-aware planning more efficient than regular planners? + Does energy-aware planning help students complete tasks compared to planners that ignore their energy throughout the day? 


**Primary measure:** percent of planned tasks completed by their due date. 
**Secondary measure:** how often students follow the suggested plan, and a short survey on how easy the plan was to follow. 
**Comparsion:** Luma with energy-aware placement on vs. Luma without the energy-aware cycle. 

## v1 scope

**In:**
- Add and edit tasks (title, due date, time estimate, difficulty)
- Add weekly commitments
- 1 to 5 energy check-in
- Weekly plan with a "why this is here" explanation for each task
- Different colors for tasks Luma placed and items the user entered

**Out (for now):**
- Energy patterns chart (needs about a month of data)
- Accounts, syncing, or mobile apps
- Notifications
- Anything that infers mood or health

## Scheduling rules (first draft)

1. Sort tasks by due date.
2. Place harder tasks in the user's higher-energy open slots.
3. Place lighter tasks in lower-energy slots.
4. Leave a buffer of at least one day before each deadline.
5. Never schedule over a commitment.
6. Write one plain-English sentence explaining each placement.

**New users (decide):** during the first one to two weeks, Luma has little
energy data, so it asks "When do you usually feel sharpest?" during setup
and tells users that suggestions improve over time.

## Tech

Python, Streamlit, Figma (design). Hosted as an open-source project on
GitHub under the MIT license.

## Risks

- **Not enough data early on:** handled by the setup question above.
- **Small pilot:** results are early signals, not proof.
- **Scope creep:** v1 stays limited to the list above.
- **Minors:** high school students need parental consent and likely school
  guidance, so early testing uses undergraduates.

## Open questions

- Will students rate their energy consistently if it takes more than a
  few seconds?
- What time blocks should the plan use (hourly, or morning, afternoon,
  evening)?
- What should Luma do when a student skips check-ins?
