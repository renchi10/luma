import streamlit as st
from datetime import date, time
from storage import load, save

st.set_page_config(page_title="Luma")

page = st.sidebar.radio(
    "Go to",
    ["Today", "Add task", "Energy check-in", "Weekly plan", "Commitments"],
)

LEVELS = {1: "Easy", 2: "Medium", 3: "Hard"}
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if page == "Today":
    st.title("Luma")
    st.write("Energy-aware planning for students.")

elif page == "Add task":
    st.header("Add a task")
    use_window = st.checkbox("Set a specific time (optional)")
    with st.form("add_task", clear_on_submit=True):
        title = st.text_input("Title")
        due = st.date_input("Due date", min_value=date.today())
        difficulty = st.select_slider(
            "Difficulty", options=[1, 2, 3], format_func=LEVELS.get
        )
        if use_window:
            start = st.time_input("From", value=time(16, 0))
            end = st.time_input("To", value=time(17, 0))
        else:
            hours = st.number_input(
                "Time needed (hours)", min_value=0.5, step=0.5, value=1.0
            )
        submitted = st.form_submit_button("Add task")

    if submitted and title:
        task = {
            "title": title,
            "due": due.isoformat(),
            "difficulty": difficulty,
            "done": False,
            "start": None,
            "end": None,
        }
        valid = True
        if use_window:
            if end <= start:
                st.error("The end time must be after the start time.")
                valid = False
            else:
                task["start"] = start.strftime("%H:%M")
                task["end"] = end.strftime("%H:%M")
                minutes = (end.hour * 60 + end.minute) - (start.hour * 60 + start.minute)
                task["hours"] = round(minutes / 60, 2)
        else:
            task["hours"] = hours
        if valid:
            tasks = load("tasks")
            tasks.append(task)
            save("tasks", tasks)
            st.success(f"Added: {title}")

    saved = load("tasks")
    if saved:
        st.subheader("Your tasks")
        st.dataframe(saved)

elif page == "Energy check-in":
    st.header("How is your energy right now?")
    part = st.selectbox("Part of day", ["morning", "afternoon", "evening"])
    cols = st.columns(5)
    for rating, col in enumerate(cols, start=1):
        if col.button(str(rating), use_container_width=True, key=f"energy{rating}"):
            ratings = load("energy")
            ratings.append({
                "date": date.today().isoformat(),
                "part": part,
                "rating": rating,
            })
            save("energy", ratings)
            st.success(f"Logged {rating} out of 5 for the {part}.")
    st.caption("1 is very low energy, 5 is very high.")

    logged = load("energy")
    if logged:
        st.subheader("Recent check-ins")
        st.dataframe(logged[-10:])

elif page == "Commitments":
    st.header("Weekly commitments")
    st.caption("Classes, practices, clubs, and other fixed events.")
    with st.form("add_commitment", clear_on_submit=True):
        name = st.text_input("Title")
        weekday = st.selectbox("Day", range(7), format_func=lambda d: DAYS[d])
        start = st.time_input("Starts", value=time(16, 0))
        end = st.time_input("Ends", value=time(18, 0))
        submitted = st.form_submit_button("Add commitment")
    if submitted and name:
        if end <= start:
            st.error("The end time must be after the start time.")
        else:
            items = load("commitments")
            items.append({
                "title": name,
                "weekday": weekday,
                "start": start.strftime("%H:%M"),
                "end": end.strftime("%H:%M"),
            })
            save("commitments", items)
            st.success(f"Added: {name}")

    items = load("commitments")
    if items:
        st.subheader("Your week")
        rows = [
            {
                "Title": i["title"],
                "Day": DAYS[i["weekday"]],
                "Starts": i["start"],
                "Ends": i["end"],
            }
            for i in sorted(items, key=lambda i: (i["weekday"], i["start"]))
        ]
        st.dataframe(rows)

else:
    st.header(page)
    st.write("Coming soon.")
