# Petri-ArvoreCobertura

A simple Python project to generate a **coverability tree** for a Petri Net.

> ⚠️ Current status: this implementation still has known errors/limitations and is a work in progress.

The main code is in [main.py](main.py), with a function that receives:

- initial marking (`m0`)
- input matrix (`Ain`)
- output matrix (`Aout`)

and returns a list of edges in the format:

`[current_marking, transition, resulting_marking]`

---

## What the program does

The `PetriToCoveringTree(m0, Ain, Aout)` function:

1. Validates input data.
2. Iterates through enabled transitions.
3. Generates new markings after firings.
4. Builds the coverability tree as a list of edges.
5. Uses a token limit (`maxcaptoken`) to avoid infinite growth, converting values to `inf` when exceeded.

---

The program prints in the terminal:

- calculated token limit
- generated coverability tree edges

## Requirements

- Python 3
- Dependencies listed in [requirements.txt](requirements.txt)

For environment setup and dependency installation commands (Linux and Windows), see the comments in [requirements.txt](requirements.txt). Create and activate the virtual environment first, then install dependencies and run the activation file.

## Project structure

- [main.py](main.py): coverability tree logic and execution example
- [README.md](README.md): project documentation
- [requirements.txt](requirements.txt): Python dependencies and setup command comments

---

## Recommendation

To help define the `Ain` and `Aout` matrices correctly, it is recommended to model and validate your Petri Net first with tools such as:

- TINA
- PIPE
- Snoopy
- other Petri Net editors/simulators

These tools can reduce manual mistakes when building matrices from places/transitions and arc weights.

---

## Note

This is an academic project (Modeling and Control of Discrete Event Systems) and represents a simplified implementation of a Petri Net coverability tree.
