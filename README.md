# luma
An open-source energy-aware planner that schedules student tasks levels and explains every suggestion towards each decision. 

**Status:** Early development. Not ready for daily use.

## What is Luma?

Most planners treat every hour equally. Luma asks how your energy is doing, learns your patterns over time, and plans tasks accordingly when you have more energy or when you have less energy. Every placement comes with an easy explaination, so you always know why a task is where it is.

Luma is built for high school and undergraduate students who are constantly juggling assignments, extracurriculars, deadlines, commitments, practices, and etc.

## Important note

 Luma is only a planning aid. It is not a medical or mental health tool, and it does not diagnose anything based on your mood. It only uses the energy ratings users enter themselves.

## How it works

1. **Add tasks:** title, due date, time estimate, and difficulty.
2. **Add commitments:** fixed events like classes, practice, or meetings.
3. **Check in:** rate your energy from 1 to 5 once or twice a day.
4. **Get a plan:** Luma matches harder tasks to times when your energy is
   usually higher and leaves a buffer before deadlines.
5. **See why:** each suggestion includes an explanation.

## Planned features

- [ ] Add and edit tasks
- [ ] Add weekly commitments
- [ ] Quick 1 to 5 energy check-in
- [ ] Weekly plan with an explanation for each suggestion
- [ ] Energy patterns view (after about a month of data)

## Research question

Does energy-aware planning help students complete tasks compared to
planners that ignore energy?

## Tech

- Python
- Streamlit
- Figma (design)

## Getting started

Setup instructions are coming once the first prototype runs. They will
look like this:

```
git clone https://github.com/YOUR-USERNAME/luma.git
cd luma
pip install -r requirements.txt
streamlit run app.py
```

## Contributing

Contributions are welcome once v1 is out. For now, feedback is the most
useful thing. Feel free to open an issue.

## License

MIT. See [LICENSE](LICENSE).
