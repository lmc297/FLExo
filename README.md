<p align="center">
    <img src="./assets/flexo_logo_v1.svg" />
</p>

# FLExo

Scalable exotoxin annotation using machine learning (ML)

# 🤖 Overview

FLExo (<ins>F</ins>ast <ins>L</ins>ocator for <ins>Exo</ins>toxins) uses a conditional random field (CRF) to identify exotoxin and exotoxin-associated genes in prokaryotic (meta)genomes.


# 🔍 Quickstart

To detect exotoxins and exotoxin-associated genes in an assembled prokaryotic (meta)genome:
```
flexo run -g [fasta] -o [output directory] [options...]
``` 

For help/to view all options:
```
flexo -h
```

# 🔧 Installation

FLExo and its dependencies can be installed via `pip`:
```
pip install flexo-tool
```

# ⚙️  Usage and options

## Command structure

```
flexo run -g [fasta] -o [output directory] [options...]
``` 

## Required arguments

```
    -g <file>, --genome <file>    a genomic file containing one or more
                                  sequences to use as input. Must be in
                                  one of the sequences format supported
                                  by Biopython.
```
