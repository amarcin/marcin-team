import streamlit as st

# "Nice. Now, on the \"________ to Heaven\", the number of a cubed triangle, you'll find the next clue."
# "Look to the east, and seek the piece, seated in the tree, to find your peace at least."

LEVELS = [
    {"puzzle": "What kind of trees are all around us?", "code": "jeffrey pines"},
    {"puzzle": "This place is special. Over this many million years has this lake been around.", "code": "2"},
    {"puzzle": "What's more, this lake is over one of these units above sea level.", "code": "mile"},
    {"puzzle": "There's a building in New York that's pretty tall. If you stood it up in the lake, it wouldn't even reach the top of the water.", "code": "empire state building"},
    {"puzzle": "One's green, called the other, and the other is very cold, called green. The water in this lake is colder than the other place.", "code": "iceland"},
    {"puzzle": "What's the name of the people that came here first?", "code": "washoe"},
    {"puzzle": "Here's a fun one. There's a famous author, with which Hayden is familiar, who accidentally set off a forest fire here.", "code": "mark twain"},
    {"puzzle": "Take A Hike, Or don't, but it'll be worth Every second", "code": "tahoe"},
    {"puzzle": "The more you take, the more you leave behind. What am I?", "code": "footstep"},
    {"puzzle": "Four people need to cross a bridge at night. They have one flashlight, and the bridge can only hold two people at a time. The four people take 1, 2, 5, and 10 minutes to cross, respectively. If two people cross together, they move at the slower person’s pace. What's the least amount of minutes they can all get across?", "code": "17"},
]

FAMILY_PROFILES = [
    {
        "display_name": "Dad",
        "age": 60,
        "role": "Trail Medic",
        "emoji1": "🩺",
        "emoji2": "👨‍⚕️",
        "desc": "Will provide a monotone diagnosis of the family trip.",
    },
    {
        "display_name": "Maret",
        "age": 28,
        "role": "Eco Hero",
        "emoji1": "🦸‍♀️",
        "emoji2": "🌱",
        "desc": "Always saving the world, even if it's just a toothbrush.",
    },
    {
        "display_name": "Gus",
        "age": 26,
        "role": "AI Navigator",
        "emoji1": "🤖",
        "emoji2": "🧠",
        "desc": "Busy spending 3 hours automating a 3 second task",
    },
    {
        "display_name": "Adrienne",
        "age": 23,
        "role": "Vintage Visionary",
        "emoji1": "🌸",
        "emoji2": "🎨",
        "desc": "Witty knitting metro retro passionate fashion masta.",
    },
    {
        "display_name": "Henry",
        "age": 13,
        "role": "Forest Freestyler",
        "emoji1": "🏀",
        "emoji2": "⛰️",
        "desc": "Thinks \"trail mix\" is a Spotify playlist.",
    },
    {
        "display_name": "Hayden",
        "age": 11,
        "role": "Family CFO: Chief Fun Officer",
        "emoji1": "🎉",
        "emoji2": "🦋",
        "desc": "Adds her own solar flair to the party!",
    },
]

st.set_page_config(page_title="Lake Tahoe Puzzle Tracker", page_icon="🧩", layout="wide")

if "profile" in st.session_state and st.session_state.profile:
    user = st.session_state.profile
    st.markdown(
        f"""
        <style>
        .tahoe-user-badge {{
            position: fixed;
            top: 4.5em;
            right: 2.2em;
            z-index: 9999;
            background: rgba(255,255,255,0.95);
            border-radius: 1.5em;
            padding: 0.7em 1.5em;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            display: flex;
            align-items: center;
            font-size: 1.1em;
            border: 1px solid #e0e0e0;
        }}
        .tahoe-user-badge .user-name {{
            font-weight: 600;
            margin-right: 0.7em;
        }}
        .tahoe-user-badge .user-role {{
            color: #4B6A34;
            font-size: 0.98em;
            background: #eaf6ea;
            border-radius: 1em;
            padding: 0.2em 0.9em;
            margin-left: 0.2em;
        }}
        </style>
        <div class='tahoe-user-badge'>
            <span class='user-name'>{user["display_name"]}</span>
            <span class='user-role'>{user["role"]}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <style>
    html, body, .stApp {
        height: 100%;
        min-height: 100vh;
        background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1500&q=80') no-repeat center center fixed;
        background-size: cover;
        color: #1a2634;
    }
    /* Add a semi-transparent light gray background to the main app content */
    .stApp > header {background: transparent !important;}
    .stApp [data-testid="stVerticalBlock"] {
        background: rgba(240, 240, 240, 0.85);
        border-radius: 18px;
        padding: 2.5em 2em 2em 2em;
        margin-top: 2em;
        margin-bottom: 2em;
        box-shadow: 0 4px 32px 0 rgba(0,0,0,0.12);
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>🌲 Lake Tahoe Marcin Adventure 🌲</h1>", unsafe_allow_html=True)

# Session state for user and progress
if "profile" not in st.session_state:
    st.session_state.profile = None
if "level" not in st.session_state:
    st.session_state.level = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

# Login with profile cards
if not st.session_state.profile:
    st.markdown("<h3 style='text-align: center;'>Choose your avatar:</h3>", unsafe_allow_html=True)
    num_profiles = len(FAMILY_PROFILES)
    num_cols = 3
    rows = (num_profiles + num_cols - 1) // num_cols
    for row in range(rows):
        cols = st.columns(num_cols)
        for col in range(num_cols):
            idx = row * num_cols + col
            if idx < num_profiles:
                profile = FAMILY_PROFILES[idx]
                with cols[col]:
                    if st.button(f"{profile['display_name']}", key=f"profile_{profile['display_name']}", use_container_width=True):
                        st.session_state.profile = profile
                        st.session_state.username = profile["display_name"]
                        st.rerun()
                    st.markdown(f"<div style='text-align:center; font-size:1.1em;'><b>{profile['emoji1']} {profile['role']} {profile['emoji2']}</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='text-align:center; color:#555;'>{profile['desc']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='text-align:center; font-size:0.9em; color:#888;'>Age: {profile['age']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height: 2em'></div>", unsafe_allow_html=True)
    st.stop()
else:
    profile = st.session_state.profile
    # Progress bar at the top
    progress = (st.session_state.level) / (len(LEVELS))
    st.markdown("<div style='height: 1em'></div>", unsafe_allow_html=True)
    st.progress(progress, text=f"Progress: {st.session_state.level} of {len(LEVELS)} puzzles completed")
    st.markdown("<div style='height: 1em'></div>", unsafe_allow_html=True)
    current_level = st.session_state.level
    if current_level >= len(LEVELS):
        st.success("Congratulations! That's all for now, folks!")
        st.stop()
    level_info = LEVELS[current_level]
    st.header(f"{level_info['puzzle']}")
    st.markdown("<div style='height: 1em'></div>", unsafe_allow_html=True)

    # --- FIX: Clear code_input before widget creation if needed ---
    if st.session_state.get("reset_code_input", False):
        st.session_state["code_input"] = ""
        st.session_state["reset_code_input"] = False

    code = st.text_input(" ", key="code_input")
    if code:
        if code.strip().lower() == level_info["code"].strip().lower():
            st.session_state.level += 1
            st.session_state.show_hint = False
            st.session_state.celebrate = True
            st.session_state.feedback = ""
            st.session_state["reset_code_input"] = True
            st.rerun()
        else:
            st.session_state.feedback = "Incorrect code. Try again!"
            st.session_state.celebrate = False
            st.session_state["reset_code_input"] = True
            st.rerun()
    if st.session_state.feedback:
        if getattr(st.session_state, 'celebrate', False):
            st.snow()
            st.success(st.session_state.feedback)
            st.session_state.celebrate = False 
        else:
            st.info(st.session_state.feedback)
    st.markdown("<div style='height: 1em'></div>", unsafe_allow_html=True)
