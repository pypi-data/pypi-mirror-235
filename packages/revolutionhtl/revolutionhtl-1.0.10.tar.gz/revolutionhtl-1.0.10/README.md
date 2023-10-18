![REvolutionH-tl logo.](https://gitlab.com/jarr.tecn/revolutionh-tl/-/raw/master/docs/images/Logo_horizontal.png)

Bioinformatics tool for the reconstruction of evolutionary histories. Input: fasta files or sequence alignment hits, Output: orthology. event-labeled gene trees, and reconciliations.

[Bioinformatics & complex networks lab](https://ira.cinvestav.mx/ingenieriagenetica/dra-maribel-hernandez-rosales/bioinformatica-y-redes-complejas/)

- José Antonio Ramírez-Rafael [jose.ramirezra@cinvestav.mx]
- Maribel Hernandez-Rosales [maribel.hr@cinvestav.mx ]

# Steps

1. **Orthogroup & best hit selection.** Input: alignment hits (generate this using `revolutionhtl.diamond`) .
2. **Orthology and gene tree reconstruction.** Input: best hits (generate this at step 1).
3. **Species tree reconstruction.** Input: gene trees (generate this at step 2).
4. **Tree reconciliation.** Input: gene and species trees (generate this at steps 2 and 3).

# Install

```bash
pip install revolutionhtl
```

**Requirements**

[Python >=3.7 ](https://www.python.org/)

If you want to run sequence alignments using revolutionhtl, then install [Diamond](https://github.com/bbuchfink/diamond).

# Usage

> Go to the [wiki](https://gitlab.com/jarr.tecn/revolutionh-tl/-/blob/master/docs/wiki.md?ref_type=heads) for details and an [example](https://gitlab.com/jarr.tecn/revolutionh-tl/-/blob/master/docs/example.md?ref_type=heads).

```bash
python -m revolutionhtl <arguments>
```

The arguments specify steps to run and parameters.

<details>
  <summary>Specify steps and input data (Click to expand)</summary> 
  <b>- -h    --help </b> show this help message and exit <br/> <br/>
  <b>-steps [int ...] </b> List of steps to run (default: 1 2 3 4).  <br/> <br/>

  <b>-alignment_h str     --alignment_hits str</b> Directory containing alignment hits, the input of step 1. (default: ./). <br/> <br/>
  <b>-best_h str     --best_hits str</b> .tsv file containing best hits, the input of step 2. (default: use output of step 1). <br/> <br/>
  <b>-T str     --gene_trees str</b> .tsv file containing gene trees, the input of steps 3 and 4. (default: use output of step 2). <br/> <br/>
  <b>-S str     --species_tree str</b> .nhx file containing a species tree, an input of step 4. (default: use output of step 3). <br/> <br/>


</details>


<img src="https://gitlab.com/jarr.tecn/revolutionh-tl/-/raw/master/docs/images/revolution_diagram.png" alt="pipeline" style="zoom:25%;" />
