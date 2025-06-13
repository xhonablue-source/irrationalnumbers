import streamlit as st
import numpy as np
import pandas as pd

# --- MathCraft Header --- (MUST BE FIRST!)
st.set_page_config(
    page_title="MathCraft | Irrational Numbers 🍰",
    layout="centered",
    page_icon="🔢"
)

# Using Streamlit's built-in charting - no matplotlib needed!

st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #56CCF2, #2F80ED); border-radius: 10px;">
    <h1 style="color: white; margin: 0; font-weight: bold;">🔢 MathCraft: Irrational Numbers</h1>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">The Cake That Wouldn't Slice Evenly!</p>
    <p style="color: #d0e8ff; margin-top: 0.5rem; font-size: 0.9rem;">By Xavier Honablue M.Ed.</p>
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

### 📜 The True History of "Logarithm" - Giving Credit Where Due
The word **"logarithm"** has a complex origin story that reveals both mathematical genius and the importance of acknowledging all contributors!

**Etymology Breakdown:**
- **"Logos"** (Greek) = word, ratio, reason
- **"Arithmos"** (Greek) = number
- **"Logarithm"** = literally "ratio number" or "the number of the ratio"

**The Real Historical Context:**
While Scottish mathematician **John Napier** coined the term "logarithm" in 1614 with his publication *Mirifici logarithmorum canonis descriptio*, the foundational concepts came from much earlier work:

**The True Foundation:**
- **Al-Kashi** (15th century Persian mathematician) developed sophisticated calculation methods using what we now recognize as logarithmic principles, creating detailed tables for exponential relationships
- **African scholars in Timbuktu** at Sankore University (13th-16th centuries) were performing complex calculations with exponential relationships centuries before European "discovery"

**What Napier Actually Did:**
Rather than inventing the concept, Napier:
1. **Systematized** existing knowledge from Arabic and African mathematical traditions
2. **Created the terminology** ("logarithm") and notation we use today
3. **Published comprehensive tables** that made the methods widely accessible in Europe
4. **Built upon centuries** of Islamic Golden Age mathematics

**Why This Matters:**
Understanding the true history shows us that mathematical knowledge is **global and collaborative**. Many "European discoveries" built on African and Arabic foundations, and credit should flow to all contributors, not just the person who coined the English term.

**Visual Connection:**
Those distinctive logarithmic curves? Islamic mathematicians were mapping these relationships centuries before European textbooks. Mathematics truly knows no borders!
""")

# Add a section break
st.markdown("---")

# --- Chart 1: Logarithmic Power Bar ---
st.subheader("How Far is 3 on the Log Scale?")

log3 = np.log10(3)

# Create data for the logarithmic scale visualization

# Show the position of log10(3) on the scale
scale_data = pd.DataFrame({
    'Position': ['10⁰ = 1', f'log₁₀(3) ≈ {log3:.3f}', '10¹ = 10'],
    'Value': [0, log3, 1],
    'Color': ['lightgray', 'red', 'lightgray']
})

st.write(f"**log₁₀(3) = {log3:.6f}**")
st.write(f"This means 3 is located at approximately **{log3*100:.1f}%** along the logarithmic scale from 1 to 10.")

# Simple bar chart showing the position
chart_data = pd.DataFrame({
    'Scale Position': [0, log3, 1],
    'Label': ['Start (10⁰=1)', 'log₁₀(3)', 'End (10¹=10)']
})

st.bar_chart(chart_data.set_index('Label')['Scale Position'])

# --- Chart 2: Cake Slicing Metaphor ---
st.subheader("The Cake That Wouldn't Slice Evenly 🎂")

st.write("Imagine trying to slice a cake at exactly the log₁₀(3) position:")

# Create a progress bar to show the "slice" position
st.write("**Cake Slice Position:**")
st.progress(log3)
st.write(f"The slice would be at {log3*100:.1f}% of the way through the cake - an irrational position that can never be cut perfectly!")

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
    🧮 Built with MathCraft | Powered by Streamlit + Python | Concept and Design by Xavier Honablue M.Ed.
</div>
""", unsafe_allow_html=True)
