import streamlit as st

# Define the password
PASSWORD = "30DayMCAT"

# Function to check the password
def check_password():
    """Returns `True` if the user entered the correct password."""
    def password_entered():
        if st.session_state["password"] == PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Enter the password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Enter the password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    # Define the table of contents as a dictionary
    table_of_contents = {
        "Biology": [
            "Ch. 1 - The Cell",
            "Ch. 2 - Reproduction",
            "Ch. 3 - Embryogenesis & Development",
            "Ch. 4 - The Nervous System",
            "Ch. 5 - The Endocrine System",
            "Ch. 6 - The Respiratory System",
            "Ch. 7 - The Cardiovascular System",
            "Ch. 8 - The Immune System",
            "Ch. 9 - The Digestive System",
            "Ch. 10 - Homeostasis",
            "Ch. 11 - The Muscular System",
            "Ch. 12 - Genetics and Evolution"
        ],
        "Chemistry": [
            "Ch. 1 - Atomic Structure",
            "Ch. 2 - Periodic Table",
            "Ch. 3 - Bonding & Chemical Interactions",
            "Ch. 4 - Compounds & Stoichiometry",
            "Ch. 5 - Chemical Kinetics",
            "Ch. 6 - Equilibrium",
            "Ch. 7 - Thermochemistry",
            "Ch. 8 - The Gas Phase",
            "Ch. 9 - Solutions",
            "Ch. 10 - Acids & Bases",
            "Ch. 11 - Oxidation-Reduction Reactions",
            "Ch. 12 - Electrochemistry"
        ],
        "Organic Chemistry": [
            "Ch. 1 - Nomenclature",
            "Ch. 2 - Isomers",
            "Ch. 3 - Bonding",
            "Ch. 4 - Analyzing Organic Reactions",
            "Ch. 5 - Alcohols",
            "Ch. 6 - Electrophilicity & Oxidation-Reduction",
            "Ch. 7 - Enolates",
            "Ch. 8 - Carboxylic Acid",
            "Ch. 9 - Carboxylic Acid Derivatives",
            "Ch. 10 - Nitrogen & Phosphorus Compounds",
            "Ch. 11 - Spectroscopy",
            "Ch. 12 - Separations & Purifications"
        ],
        "Biochemistry Chemistry": [
            "Ch. 1 - Amino Acids Peptides & Proteins",
            "Ch. 2 - Enzymes",
            "Ch. 3 - Non-Enzyme Protein Function & Analysis",
            "Ch. 4 - Carbohydrate Structure & Function",
            "Ch. 5 - Lipid Structure and Function",
            "Ch. 6 - DNA & Biotechnology",
            "Ch. 7 - DNA Replication",
            "Ch. 8 - RNA & Genetic Codes",
            "Ch. 9 - Biological Membranes",
            "Ch. 10 - Metabolic Pathways",
            "Ch. 11 - Aerobic Respiration",
            "Ch. 12 - Lipid & Amino Acid Metabolism",
            "Ch. 13 - Bioenergetics & Metabolism Regulation"
        ],
        "Behavioral Science (Psychology & Sociology)": [
            "Ch. 1 - Biology & Behavior",
            "Ch. 2 - Sensation & Perception",
            "Ch. 3 - Learning & Memory",
            "Ch. 4 - Cognition, Consciousness & Language",
            "Ch. 5 - Motivation, Emotion & Stress",
            "Ch. 6 - Identity & Personality",
            "Ch. 7 - Psychological Disorders",
            "Ch. 8 - Social Processes, Attitude & Behaviours",
            "Ch. 9 - Social Interaction",
            "Ch. 10 - Social Thinking",
            "Ch. 11 - Social Structure & Demographics",
            "Ch. 12 - Social Stratification"
        ],
        "Math & Physics": [
            "Ch. 1 - Kinematics & Dynamics",
            "Ch. 2 - Work & Energy",
            "Ch. 3 - Thermodynamics",
            "Ch. 4 - Fluids",
            "Ch. 5 - Electrostatic and Magnetism",
            "Ch. 6 - Circuits",
            "Ch. 7 - Waves and Sounds",
            "Ch. 8 - Light and Optics",
            "Ch. 9 - Atomic Nuclear and Phenomena",
            "Ch. 10 - Mathematics",
            "Ch. 11 - Design Reasoning & Research Execution",
            "Ch. 12 - Data Base & Statistical Reasoning"
        ]
    }

    # Create sidebar navigation
    st.sidebar.title("Table of Contents")
    section = st.sidebar.selectbox("Select a Section", list(table_of_contents.keys()))
    chapter = st.sidebar.selectbox("Select a Chapter", table_of_contents[section])

    # Display the selected section and chapter
    st.title(f"{section} - {chapter}")

    # Add content for each chapter here
    # For now, just display a placeholder text
    st.write(f"Content for {chapter} will be added here.")

    # To run the app, save this code in a file, e.g., `textbook_app.py`, and run `streamlit run textbook_app.py` in your terminal.
