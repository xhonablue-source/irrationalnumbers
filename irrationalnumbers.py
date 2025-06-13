import streamlit as st
import numpy as np

# Check if matplotlib is available, if not provide alternative
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    st.error("Matplotlib is not installed. Install it with: pip install matplotlib")

# --- MathCraft Header ---
st.set_page_config(
    page_title="MathCraft | Irrational Numbers 🍰",
    layout="centered",
    page_icon="🔢"
)

st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #56CCF2, #2F80ED); border-radius: 10px;">
    <h1 style="color: white; margin: 0; font-weight: bold;">🔢 MathCraft: Irrational Numbers</h1>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">The Cake That Wouldn't Slice Evenly!</p>
    <p style="color: #d0e8ff; margin-top: 0.5rem; font-size: 0.9rem;">By Xavier Honablue</p>
</div>
""", unsafe_allow_html=True)

st.write("""
### 🧠 What is an Irrational Number?
An irrational number:
- Cannot be written as a simple fraction
- Has a decimal that goes on forever without repeating

Example: `log₁₀(3) ≈ 0.477121...`

### 🍰 Funny Analogy:
Imagine slicing a birthday cake exactly at `log₁₀(3)`. No matter how you try, you'll never cut a clean piece—it's always just off! That's what irrational numbers are like in the real world.
""")

if HAS_MATPLOTLIB:
    # --- Chart 1: Logarithmic Power Bar ---
    st.subheader("How Far is 3 on the Log Scale?")
    
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.hlines(y=1, xmin=0, xmax=1, color='lightgray', linewidth=10)
    ax.text(0, 1.1, '10⁰ = 1', ha='center', va='bottom', fontsize=12)
    ax.text(1, 1.1, '10¹ = 10', ha='center', va='bottom', fontsize=12)
    
    log3 = np.log10(3)
    ax.vlines(x=log3, ymin=0.95, ymax=1.05, color='red', linestyle='--', linewidth=2)
    ax.text(log3, 1.15, 'log₁₀(3) ≈ 0.477', color='red', ha='center', fontsize=12)
    ax.text(log3, 0.85, '≈ 47.7% of full power', color='red', ha='center', fontsize=10)
    
    ax.set_ylim(0.8, 1.3)
    ax.set_xlim(-0.05, 1.05)
    ax.axis('off')
    st.pyplot(fig)
    
    # --- Chart 2: Cake Slicing Metaphor ---
    st.subheader("The Cake That Wouldn't Slice Evenly 🎂")
    
    fig_story, ax_story = plt.subplots(figsize=(10, 2))
    slices = np.linspace(0, 1, 12)
    for s in slices:
        ax_story.axvline(s, color='gray', linestyle='--', linewidth=0.5)
    
    ax_story.axvline(log3, color='red', linewidth=2, linestyle='--', label='log₁₀(3) slice')
    ax_story.set_xticks([0, log3, 1])
    ax_story.set_xticklabels(['Start of Cake', 'log₁₀(3)', 'End of Cake'])
    ax_story.set_yticks([])
    ax_story.legend(loc='upper right')
    st.pyplot(fig_story)
    
else:
    # Fallback content when matplotlib is not available
    st.subheader("Mathematical Details")
    log3 = np.log10(3)
    st.write(f"**log₁₀(3) = {log3:.6f}**")
    st.write(f"This means 3 is located at approximately {log3*100:.1f}% along the logarithmic scale from 1 to 10.")
    
    st.subheader("Visualization Alternative")
    st.write("Install matplotlib to see the interactive charts!")
    st.code("pip install matplotlib", language="bash")

# --- Additional Information ---
st.subheader("🔍 More About Irrational Numbers")

col1, col2 = st.columns(2)

with col1:
    st.write("**Famous Irrational Numbers:**")
    st.write("- π (pi) ≈ 3.14159...")
    st.write("- e (Euler's number) ≈ 2.71828...")
    st.write("- √2 ≈ 1.41421...")
    st.write("- φ (golden ratio) ≈ 1.61803...")

with col2:
    st.write("**Properties:**")
    st.write("- Non-terminating decimals")
    st.write("- Non-repeating patterns")
    st.write("- Cannot be expressed as fractions")
    st.write("- Found everywhere in nature!")

# Interactive calculation
st.subheader("🧮 Calculate Your Own Logarithm")
number = st.number_input("Enter a number to find its log₁₀:", min_value=0.01, value=3.0, step=0.1)
if number > 0:
    result = np.log10(number)
    st.write(f"log₁₀({number}) = **{result:.8f}**")
    
    if abs(result - round(result)) < 0.0001:
        st.success("This is very close to a rational number!")
    else:
        st.info("This appears to be irrational - the decimal goes on forever!")

# --- Footer ---
st.markdown("""
<div style="text-align: center; font-size: 0.9rem; margin-top: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 5px;">
    🧮 Built with MathCraft | Powered by Streamlit + Python | Concept and Design by Xavier Honablue
</div>
""", unsafe_allow_html=True)
