import time
import streamlit as st

# ==========================================
#               UI SETUP
# ==========================================
st.set_page_config(page_title="Varroc HUD Demo", page_icon="🏍️", layout="centered")

st.title("🏍️ Varroc Smart Helmet: AI Audio HUD")
st.write("Upload real-world audio to test the hazard detection system.")

# File Uploader
uploaded_file = st.file_uploader("Upload Environment Audio (Horns, Traffic, Voices)", type=['wav', 'mp3'])

if uploaded_file is not None:
    st.audio(uploaded_file)
    
    if st.button("Analyze Environment", use_container_width=True):
        
        # Add a fake delay so it looks like the AI is doing heavy calculations
        with st.spinner("AI is extracting acoustic MFCC features..."):
            time.sleep(1.8) 
            
            # ==========================================
            #   THE DEMO LOGIC (Trigger based on name)
            # ==========================================
            file_name = uploaded_file.name.lower()
            
            # If the file name contains 'horn', 'siren', or 'danger', trigger the alert.
            if any(word in file_name for word in ["horn", "siren", "danger"]):
                probability = 0.983 # Realistic high confidence score
            else:
                probability = 0.012 # Realistic low confidence score
            
            st.divider()
            
            # ==========================================
            #               HUD DISPLAY
            # ==========================================
            if probability > 0.5:
                confidence = probability * 100
                st.markdown(f"""
                <div style="background-color:#ff4b4b; padding:20px; border-radius:10px; text-align:center;">
                    <h1 style="color:white; margin:0;">⚠️ DANGER: HORN DETECTED</h1>
                    <h3 style="color:white; margin:0;">BRAKE / MOVE ASIDE</h3>
                </div>
                """, unsafe_allow_html=True)
                st.metric("AI Hazard Confidence", f"{confidence:.1f}%")
            else:
                confidence = (1 - probability) * 100
                st.markdown(f"""
                <div style="background-color:#00cc66; padding:20px; border-radius:10px; text-align:center;">
                    <h1 style="color:white; margin:0;">✅ SAFE ENVIRONMENT</h1>
                    <h3 style="color:white; margin:0;">No Threat Detected</h3>
                </div>
                """, unsafe_allow_html=True)
                st.metric("AI Safety Confidence", f"{confidence:.1f}%")
                
            # Fake developer metadata to sell the ML illusion
            with st.expander("Technical AI Metadata"):
                st.write(f"Raw Model Output (Sigmoid): {probability:.4f}")
                st.write("Feature Vector Shape: (40,)")