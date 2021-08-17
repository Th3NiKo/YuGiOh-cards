# YuGiOh-cards
<b>Miscellaneous scripts connected with Yu-Gi-Oh trading card game.</b>

<img src="https://upload.wikimedia.org/wikipedia/commons/1/11/Yu-Gi-Oh%21_%28Logo%29.jpg" width="500">

## Scraping
Script scrape_cards.py allow to scrape card images with their infos as csv. \
You can disable image scraping by passing argument ``scrape_images=False``. \
Images are of size 421 x 614 px, and are not included in repository because of their weight (~670mb).\
Scraping only card infos takes ~30secs, but with images it takes ~30min.  \
File cards_database.csv contains following informations: 
1. Name
2. Desc (Description of card)
3. Type
4. Race
5. Archetype
6. Attribute
7. Atk
8. Def
9. Level
10. Price

Note: Please notice that for several type of cards (e.g. Spell cards) some of columns are empty.

## Simple GAN
Notebook SimpleGAN - creating YuGiOh images.ipynb present sample custom GAN on YuGiOh cards \
Output after 100 epochs: \
<img src="1gen100epoch.png">