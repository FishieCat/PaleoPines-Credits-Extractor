# PaleoPines-Credits-Extractor
Extracts Paleo Pine credits into Mobygames import format

0. Have Python and bash, like for [Arma-Reforger-Credits-Extractor](https://github.com/FishieCat/Arma-Reforger-Credits-Extractor)
1. Extract all files using [AssetRipper](https://github.com/AssetRipper/AssetRipper)
2. Place `Credits.json` from the `Assets\` folder and `UIStrings.csv` from `Assets\StreamingAssets\Strings` into an empty folder together with the script from this repository and run `python moby_json_paleopines.py Credits.json UIStrings.csv`
3. Clean up the content. It duplicates lead roles and has at least 1 typo (Parner Manager) and some ALLCAPS. Voiceover roles need manual (let's be honest—regex) cleanup.
