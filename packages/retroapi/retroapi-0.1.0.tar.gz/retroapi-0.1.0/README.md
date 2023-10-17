## RetroSynthesis API

- retroapi get predict routes given target molecule.

- supply plausible value for all predicts.

- predict conditions base on one reaction.

### Usage

```python

from retroapi import RetroApi, Name2Smiles

retro_api = RetroApi()

# if you have simles of molecule.
smiles = "COc1cccc(OC(=O)/C=C/c2cc(OC)c(OC)c(OC)c2)c1"

# else:
chemical_name = "4-Hydroxycoumarin"
name2smiles = Name2Smiles()
smiles = name2smiles.get_smiles(chemical_name)

# check if smiles is valid or not
is_valid_smiles = retro_api.validate_smiles(smiles)

if is_valid_smiles:
    routes = retro_api.predict_routes(smiles)
    if routes is not None:
        # work with routes
        pass

# check if chemical is buyable or not
is_buyable = retro_api.check_stock(smiles)

# check reaction conditions

# first you should get product smile
# second you should get reactants smile

products = "COc1cc(C(=O)O)cc(OC)c1OC"
reactants = "C=CC(=O)O.COc1cc(Br)cc(OC)c1OC"

conds = retro_api.process_reaction(product, reactants)
if conds is not None:
    # check reaction condition with plausible
    pass
```
