import pandas as pd 
import streamlit as st 
import altair as alt 
from PIL import Image

###############################
# Page Title
###############################

image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

##########################
# Input Text Box
##########################
st.header('Enter DNA sequnce')

sequence_input =">DNA Query \nGAACACGTAGG"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence #this will show the list
sequence = sequence[1:] #skips the sequence name (first line)
sequence = ''.join(sequence) #concatenates list to string

st.write(""" 
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

##DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print Dictionary