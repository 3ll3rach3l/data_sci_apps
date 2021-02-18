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
sequence = '\n'.join(sequence) #concatenates list to string

st.write(""" 
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

##DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())