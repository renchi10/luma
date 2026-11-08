import streamlit as st
from datetime import date
from storage import load, save

st.set_page_config(page_title="Luma")

page = st.sidebar.radio(
    "Go to",
    ["Today", "Add task", "Energy check-in", "Weekly plan", "Commitments"],
)

LEVELS = {1: "Easy", 2: "Medium", 3: "Hard"}

if page == "Today":
    st.title("Luma")
    st.write("Energy-aware planning for students.")

elif page == "Add task":
    st.header("Add a task")
    with st.form("add_task", clear_on_submit=True):
        title = st.text_input("Title")
        due = st.date_input("Due date", min_value=date.today())
        hours = st.number_input("Time needed (hours)", min_value=0.5, step=0.5, value=1.0)
        difficulty = st.select_slider(
            "Difficulty", options=[1, 2, 3], format_func=LEVELS.get
        )
        submitted = st.form_submit_button("Add task")
    if submitted and title:
        tasks = load("tasks")
        tasks.append({
            "title": title,
            "due": due.isoformat(),
            "hours": hours,
            "difficulty": difficulty,
            "done": False,
        })
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

else:
    st.header(page)
    st.write("Coming soon.")
