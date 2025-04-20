# PaleoPines-Credits-Extractor
Extracts Paleo Pine credits into Mobygames import format

0. Have Python and bash, like for [Arma-Reforger-Credits-Extractor](https://github.com/FishieCat/Arma-Reforger-Credits-Extractor)
1. Extract all files using [AssetRipper](https://github.com/AssetRipper/AssetRipper)
2. Place `Credits.json` from the `Assets\` folder and `UIStrings.csv` from `Assets\StreamingAssets\Strings` into an empty folder together with the script from this repository and run `python moby_json_paleopines.py Credits.json UIStrings.csv`
3. Clean up `Credits.json_moby.txt`. It contains duplicate lead roles and at least 1 typo (Parner Manager) as well as some ALLCAP groups. Voiceover roles need manual (read: regex) cleanup.
