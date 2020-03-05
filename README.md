Style generator
---------------

Generate randomly formatted rich text from a raw text.

# Example

Input text:

```raw
Chanson d'automne


Les sanglots longs
Des violons
De l'automne
Blessent mon coeur
D'une langueur
Monotone.

Tout suffocant
Et blême, quand
Sonne l'heure,
Je me souviens
Des jours anciens
Et je pleure

Et je m'en vais
Au vent mauvais
Qui m'emporte
Deçà, delà,
Pareil à la
Feuille morte.
```

Run:

```bash
$ python3 stylegen.py examples/chanson_automne.txt exemples/chanson_automne.html
```

Output:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Chanson d'automne</title>
  </head>
  <body>
  <h1>Chanson d'automne</h1>
<div>
<span style="color:black;font-size:100%">Les </span>
<i><span style="color:cyan;font-size:100%">sanglots </span></i>
<b><span style="color:cyan;font-size:50%">longs </span></b>
</div>
<div>
<b><span style="color:green;font-size:100%">Des </span></b>
<b><span style="color:green;font-size:100%">violons </span></b>
</div>
<div>
<span style="color:black;font-size:100%">De </span>
<span style="color:black;font-size:100%">l'automne </span>
</div>
<div>
<span style="color:red;font-size:100%">Blessent </span>
<b><span style="color:green;font-size:100%">mon </span></b>
<span style="color:black;font-size:100%">coeur </span>
</div>
<div>
<b><span style="color:magenta;font-size:200%">D'une </span></b>
<span style="color:black;font-size:100%">langueur </span>
</div>
<div>
<span style="color:black;font-size:100%">Monotone. </span>
</div>
<br/>
<div>
<span style="color:black;font-size:100%">Tout </span>
<span style="color:blue;font-size:200%">suffocant </span>
</div>
<div>
<span style="color:black;font-size:100%">Et </span>
<span style="color:cyan;font-size:100%">blême, </span>
<span style="color:black;font-size:100%">quand </span>
</div>
<div>
<span style="color:black;font-size:100%">Sonne </span>
<span style="color:black;font-size:100%">l'heure, </span>
</div>
<div>
<span style="color:green;font-size:100%">Je </span>
<span style="color:blue;font-size:200%">me </span>
<span style="color:black;font-size:100%">souviens </span>
</div>
<div>
<span style="color:black;font-size:100%">Des </span>
<span style="color:black;font-size:100%">jours </span>
<span style="color:cyan;font-size:200%">anciens </span>
</div>
<div>
<u><span style="color:magenta;font-size:200%">Et </span></u>
<span style="color:black;font-size:100%">je </span>
<span style="color:black;font-size:100%">pleure </span>
</div>
<br/>
<div>
<b><span style="color:black;font-size:200%">Et </span></b>
<span style="color:black;font-size:100%">je </span>
<b><span style="color:black;font-size:50%">m'en </span></b>
<span style="color:black;font-size:100%">vais </span>
</div>
<div>
<span style="color:black;font-size:100%">Au </span>
<u><span style="color:blue;font-size:50%">vent </span></u>
<u><span style="color:blue;font-size:50%">mauvais </span></u>
</div>
<div>
<span style="color:black;font-size:100%">Qui </span>
<span style="color:black;font-size:100%">m'emporte </span>
</div>
<div>
<i><span style="color:cyan;font-size:200%">Deçà, </span></i>
<b><span style="color:cyan;font-size:50%">delà, </span></b>
</div>
<div>
<span style="color:black;font-size:100%">Pareil </span>
<span style="color:blue;font-size:100%">à </span>
<span style="color:black;font-size:100%">la </span>
</div>
<div>
<b><span style="color:blue;font-size:200%">Feuille </span></b>
<b><span style="color:red;font-size:200%">morte. </span></b>
</div>  </body>
</html>
```
