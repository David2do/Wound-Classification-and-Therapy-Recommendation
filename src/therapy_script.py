"""
This module contains the therapies to be applied to the predicted wound class and its' status

main_class_name = ['Abrasion', 'Bruises', 'Burns', 'Incision', 'Laceration', 'Puncture', 'Ulcer']
status_class_name = ['Fresh', 'Healing']
# note st as streamlit
"""
import streamlit as st

def therapy(wound_class, wound_status):

    # Abrasion
    if wound_class == 'Abrasion':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 15-20\u00B0C')
            st.write('Airflow Rate: 1.5-2 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: Every 3-4 hrs for 24 hours')
            st.write('Special Recommendation: Ensure the wound is clean and dry before airflow application')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-42\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: 2-3 times daily')
            st.write('Special Recommendation: Prevent excessive drying of regenerating skin')

    # Bruises
    elif wound_class == 'Bruises':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 12-15\u00B0C')
            st.write('Airflow Rate: 1.5-2 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: Every 1-2 hrs for 24-48 hours')
            st.write('Special Recommendation: Use higher airflow to provide effective cooling to the bruised area')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-40\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: 2 times daily')
            st.write('Special Recommendation: Promote circulation in the affected area for quicker recovery')

    # Burns
    elif wound_class == 'Burns':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 18-22\u00B0C')
            st.write('Airflow Rate: 1-2 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: Every 3-4 hrs for 24-48 hours')
            st.write('Special Recommendation: Avoid airflow directly on exposed nerve ending; use a buffer zone')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 37-40\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: 1-2 times daily')
            st.write('Special Recommendation: Gradually increase temperature to avoid irritation of healing skin')

    # Incision
    elif wound_class == 'Incision':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 15-18\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: Every 2 hrs for 48 hours')
            st.write('Special Recommendation: Avoid high-pressure airflow to prevent stain on sutured edges')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-40\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: 2 times daily')
            st.write('Special recommendation: Use mild heat to avoid irritation of sutured areas')

    # Laceration
    elif wound_class == 'Laceration':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 15-20\u00B0C')
            st.write('Airflow Rate: 1-2 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: Every 2-3 hrs for 48 hours')
            st.write('Special Recommendation: Ensure gentle airflow to avoid disturbing wound edges')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-42\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: 2-3 times daily')
            st.write('Special Recommendation: Maintain uniform airflow and avoid overheating surrounding healthy tissue')

    # Puncture
    elif wound_class == 'Puncture':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 15-18\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: Every 3 hrs for 48 hours')
            st.write('Special Recommendation: Focus airflow on the wound opening; avoid highspeed air to reduce infection risk')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-42\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 15-20 minutes')
            st.write('Frequency: 2-3 times daily')
            st.write('Special Recommendation: Ensure deeper penetration of heat while avoiding overheating')

    # Ulcer
    elif wound_class == 'Ulcer':
        if wound_status == 'Fresh':
            st.write('Therapy: Cold air')
            st.write('Temperature: 15-20\u00B0Cr')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: Every 2-3 hrs for 48 hours')
            st.write('Special Recommendation: Keep the wound clean and dry; avoid overcooling surrounding tissues')
        elif wound_status == 'Healing':
            st.write('Therapy: Hot air')
            st.write('Temperature: 38-42\u00B0C')
            st.write('Airflow Rate: 1-1.5 m/s')
            st.write('Duration: 10-15 minutes')
            st.write('Frequency: 2 times daily')
            st.write('Special Recommendation: Avoid high airflow pressure to prevent discomfort in sensitive areas')



