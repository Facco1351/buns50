with open('D:/code/buns50/menu.html', encoding='utf-8') as f:
    content = f.read()

header = content[:5678]
footer = content[26249:]

def item(name, price, desc=''):
    pf = ("%.2f" % price).replace('.', ',')
    desc_html = '<span class="mi-desc">%s</span>' % desc if desc else ''
    return (
        '\n      <div class="menu-item">'
        '\n        <div class="mi-info"><span class="mi-name">%s</span>%s</div>'
        '\n        <div class="mi-right"><span class="mi-price">%s</span>'
        '<button class="mi-add" onclick="addItem(this,\'%s\',%s)">+</button></div>'
        '\n      </div>' % (name, desc_html, '€'+pf, name, price)
    )

def sec(id_, t1, t2, note=''):
    note_html = '<p class="cat-note">%s</p>' % note if note else ''
    return (
        '\n\n<!-- ====== %s ====== -->'
        '\n<section class="cat-section" id="%s">'
        '\n  <div class="container">'
        '\n    <div class="cat-hd"><h2 class="cat-title">%s<span>%s</span></h2>%s</div>' % (
            (t1+t2).upper(), id_, t1, t2, note_html)
    )

def grid(cols1=False):
    return '    <div class="items-grid%s">' % (' cols-1' if cols1 else '')

EG = '    </div>'
ES = '  </div>\n</section>'

tabs = '''<!-- ====== STICKY TABS ====== -->
<div class="mp-subnav">
  <div class="container">
    <div class="mp-tabs">
      <a href="#antipasti"   class="mp-tab">Antipasti</a>
      <a href="#fritti"      class="mp-tab">Fritti</a>
      <a href="#signature"   class="mp-tab">Signature</a>
      <a href="#burgers"     class="mp-tab">Burgers</a>
      <a href="#panini"      class="mp-tab">Panini</a>
      <a href="#hotdogs"     class="mp-tab">Hot Dogs</a>
      <a href="#poke"        class="mp-tab">Poke Bowl</a>
      <a href="#extra"       class="mp-tab">Extra</a>
      <a href="#salse"       class="mp-tab">Salse</a>
      <a href="#dolci"       class="mp-tab">Dolci</a>
      <a href="#bevande"     class="mp-tab">Bevande</a>
      <a href="#drinklist"   class="mp-tab">Drink List</a>
      <a href="#birre"       class="mp-tab">Birre</a>
      <a href="#vini"        class="mp-tab">Vini</a>
      <a href="#amari"       class="mp-tab">Amari</a>
    </div>
  </div>
</div>
'''

b = tabs

# ANTIPASTI
b += sec('antipasti','ANTI','PASTI','Starters')
b += '\n' + grid()
b += item('Olive', 2.00)
b += item('Nachos con Salsa Mex', 4.00)
b += item('Mortadella alla Brace', 7.50)
b += item('Gamberoni al Panko con Salsa Sweet Chili', 10.00, '5 pezzi - Homemade')
b += '\n' + EG
b += '\n' + ES

# FRITTI
b += sec('fritti','FRI','TTI')
b += '\n' + grid()
b += item('Buns Chips', 4.00)
b += item('Sweet Potatoes Fries', 6.00)
b += item('Onion Rings', 6.00, '10 pezzi')
b += item('Cheddar e Bacon Chips', 6.50)
b += item('Chips alla Gricia', 7.00, 'Guanciale e Salsa Cacio e Pepe Homemade')
b += item('Jalapeno Red Hot', 7.50, '5 pezzi - Peperoncino rosso panato ripieno di crema di formaggio')
b += item('Fried Chicken', 8.00, '8 pezzi')
b += '\n' + EG
b += '\n' + ES

# SIGNATURE
b += '\n\n<!-- ====== SIGNATURE ====== -->'
b += '\n<section class="cat-section" id="signature">'
b += '\n  <div class="container">'
b += '\n    <div class="cat-hd"><h2 class="cat-title">BUNS <span>BURGER</span></h2><p class="cat-note">Il nostro panino Signature</p></div>'
b += '\n' + grid(True)
b += item('Buns Burger', 13.50, 'Doppio Burger di Scottona, Formaggio Fuso, Capocollo di Martina Franca IGP, Salsa Miele Mostarda, Insalata, Pomodori Secchi, Granella di Pistacchio')
b += '\n' + EG
b += '\n' + ES

# BURGERS
b += sec('burgers','BUR','GERS','Anche in versione smash')
b += '\n' + grid()
b += item('Classic Burger', 8.00, 'Hamburger di Scottona, Insalata, Pomodoro, Ketchup, Maionese')
b += item('Smoke Burger', 9.50, 'Hamburger di Scottona, Maionese Affumicata al Bacon, Doppio Cheddar, Bacon Crispy')
b += item('North Caroline', 10.00, 'Pulled Pork, Coleslaw, Doppio Cheddar, Doppio Bacon, Salsa BBQ, Maionese')
b += item('Chicken Burger', 10.00, 'Pollo Fritto Panato al Panko Homemade, Insalata, Pomodoro, Doppio Cheddar, Doppio Bacon, Salsa Buns')
b += item('Crispy Buns Bacon', 10.00, 'Hamburger di Scottona, Triplo Cheddar, Triplo Bacon, Salsa Buns')
b += item('Cheese Burger', 10.00, 'Hamburger di Scottona, Doppio Cheddar, Cipolla Bianca a Dadini, Cetrioli Pickles, Senape, Ketchup')
b += item('Veg Burger', 10.00, 'Hamburger di Lenticchie e Spinacino Homemade, Insalata, Pomodoro, Salsa Buns o Mayo Vegana')
b += item('Cancun', 11.00, 'Hamburger di Scottona, Doppio Cheddar, Doppio Bacon, Salsa Yogurt, Jalapeno, Insalata, Nachos Sbriciolato')
b += item('Roma', 11.00, 'Hamburger di Scottona, Salsa Cacio e Pepe Homemade, Insalata, Guanciale, Uovo alla Piastra')
b += item('Dublin', 13.50, 'Hamburger di Angus Irlandese, Doppio Cheddar, Doppio Bacon, Cipolla Caramellata Homemade, Senape, Ketchup')
b += item('Belfast', 13.50, 'Hamburger di Angus Irlandese, Insalata, Pomodoro, Triplo Bacon, Triplo Cheddar, Salsa BBQ, Maionese, Cipolla Crispy')
b += '\n' + EG
b += '\n' + ES

# PANINI
b += sec('panini','PAN','INI')
b += '\n' + grid()
b += item('Bologna', 7.50, 'Mortadella di Bologna, Stracciatella, Pomodori Secchi, Granella di Pistacchio')
b += item('Martina Franca', 8.00, 'Capocollo di Martina Franca IGP, Bufala, Pomodori Secchi, Insalata')
b += item('Tonnetto', 10.00, 'Tartare di Tonno Fresco, Insalata, Pomodoro, Stracciatella, Tabasco')
b += item('Norway', 10.00, 'Tartare di Salmone Fresco, Bufala, Insalata, Pomodoro, Granella di Pistacchio, Maionese alla Soia')
b += '\n' + EG
b += '\n' + ES

# HOT DOGS
b += sec('hotdogs','HOT ','DOGS')
b += '\n' + grid()
b += item('Classic Hot Dog', 6.00, 'Wurstel, Ketchup, Maionese')
b += item('Berlino', 7.00, 'Wurstel, Crauti, Senape, Ketchup')
b += item('Vienna', 8.00, 'Wurstel, Crauti, Cipolla Crispy, Senape, Ketchup')
b += item('Tulum', 8.50, 'Wurstel, Cheddar Fuso, Bacon Crispy, Jalapeno Verdi a Rondelle, Salsa BBQ, Maionese')
b += item('Los Angeles', 9.00, 'Wurstel, Cheddar Fuso, Bacon Crispy, Cipolla Caramellata Homemade, Senape, Ketchup')
b += '\n' + EG
b += '\n' + ES

# POKE
b += sec('poke','POKE ','BOWL')
b += '\n' + grid()
b += item('Corfu', 9.00, 'Riso Basmati, Insalata, Pomodoro, Olive Nere, Cetriolo, Feta, Cipolla Rossa, Salsa Yogurt')
b += item('Thai', 10.00, 'Riso Basmati, Insalata, Pomodoro, Carote, Olive Nere, Pollo alla Griglia, Salsa Curry')
b += item('Oslo', 11.00, 'Riso Basmati, Tartare di Salmone Fresco, Insalata, Semi Misti, Pomodoro, Avocado, Granella di Pistacchio, Salsa Yogurt, Stracciatella')
b += item('Tuna', 12.00, 'Riso Basmati, Tartare di Tonno Fresco, Insalata, Pomodoro, Bufala, Mango, Semi Misti, Soia')
b += '\n' + EG
b += '\n' + ES

# EXTRA
b += sec('extra','EX','TRA','Aggiunte al panino')
b += '\n' + grid()
b += item('Burger di Scottona', 3.00)
b += item('Pulled Pork', 3.00)
b += item('Bun Gluten-Free', 2.00)
b += item('Bacon', 1.50)
b += item('Cheddar', 1.00)
b += item('Mozzarella Senza Lattosio', 1.00)
b += item('Burger di Angus', 4.00)
b += '\n' + EG
b += '\n' + ES

# SALSE
b += sec('salse','SAL','SE','Tutte a 0,50')
b += '\n' + grid()
for s in ['Buns','BBQ','Miele e Mostarda','Yogurt','Curry','Cacio e Pepe','Sweet Chili','Cheddar','Maionese','Ketchup','Salsa Mex','Salsa Smoke']:
    b += item(s, 0.50)
b += '\n' + EG
b += '\n' + ES

# DOLCI
b += sec('dolci','DOL','CI')
b += '\n' + grid(True)
b += item('Dolci del giorno', 5.00, 'A seconda delle disponibilita - chiedi al personale')
b += '\n' + EG
b += '\n' + ES

# BEVANDE
b += sec('bevande','BEV','ANDE','Analcoliche')
b += '\n' + grid()
b += item('Acqua Naturale', 2.00)
b += item('Acqua Frizzante', 2.00)
b += item('Coca Cola', 2.50)
b += item('Coca Cola Zero', 2.50)
b += item('Fanta', 2.50)
b += item('Sprite', 2.50)
b += item('Lemonsoda', 2.50)
b += item('The alla Pesca', 2.50)
b += item('The al Limone', 2.50)
b += item('Ginger Beer', 3.00)
b += '\n' + EG
b += '\n' + ES

# DRINK LIST
b += sec('drinklist','DRINK','LIST','Cocktail & Spirits')
b += '\n' + grid()
b += item('Campari', 3.00)
b += item('Aperol Spritz', 5.00)
b += item('Campari Spritz', 5.00)
b += item('London Hill', 6.00)
b += item('London N.3', 7.50)
b += item('Hendricks', 7.50)
b += item('Gin Mare', 8.00)
b += '\n' + EG
b += '\n' + ES

# BIRRE
b += sec('birre','BIR','RE')
b += '\n    <p class="eyebrow" style="margin-bottom:20px">Alla Spina</p>'
b += '\n' + grid(True)
b += item('Birra Moretti 0,40cl', 4.00, '4,6% vol.')
b += item('Birra Moretti 0,20cl', 2.50, '4,6% vol.')
b += '\n' + EG
b += '\n    <p class="eyebrow" style="margin-top:40px;margin-bottom:20px">In Bottiglia</p>'
b += '\n' + grid(True)
b += item('Menabrea Bionda', 3.00, 'Chiara a Bassa Fermentazione - 4,8% vol. - Italia')
b += item('Menabrea Rossa', 3.50, 'Doppio Malto - 7,5% vol. - Italia')
b += item('Slalom', 3.50, 'Lager Strong - 9% vol. - Scozia')
b += item('Bjorne Beer', 3.50, 'Lager Strong - 8,3% vol. - Danimarca')
b += item('Estrella Daura Gluten Free', 4.50, 'Lager - 5% vol. - Spagna')
b += item('Erdinger', 5.00, 'Weiss - 5,3% vol. - Germania')
b += item('Chimay', 5.00, 'Abbazia/Trappiste - 7% vol. - Belgio')
b += '\n' + EG
b += '\n' + ES

# VINI
b += sec('vini','VI','NI','In bottiglia - 75cl')
b += '\n    <p class="eyebrow" style="margin-bottom:20px">Rosati</p>'
b += '\n' + grid(True)
b += item('Tramari', 20.00, 'Primitivo 100% - 13% vol. - Puglia')
b += item('Domodo', 20.00, 'Primitivo 100% - 12% vol. - Puglia')
b += '\n' + EG
b += '\n    <p class="eyebrow" style="margin-top:40px;margin-bottom:20px">Rossi</p>'
b += '\n' + grid(True)
b += item('Talo Negroamaro', 20.00, 'Negroamaro 100% - 13,5% vol. - Puglia')
b += item('Talo Primitivo', 20.00, 'Primitivo 100% - 14% vol. - Puglia')
b += '\n' + EG
b += '\n    <p class="eyebrow" style="margin-top:40px;margin-bottom:20px">Bianchi & Bollicine</p>'
b += '\n' + grid(True)
b += item('Talo Chardonnay', 20.00, 'Chardonnay 100% - 13% vol. - Puglia')
b += item('Prosecco', 15.00, 'Bollicine italiane')
b += '\n' + EG
b += '\n' + ES

# AMARI
b += sec('amari','AMARI E ','DISTILLATI')
b += '\n' + grid()
b += item('Montenegro', 2.50)
b += item('Amaro del Capo', 2.50)
b += item('Jagermeister', 2.50)
b += item('Limoncello', 2.50)
b += item('Grappa 903 Barricata', 3.50)
b += item('Jameson', 5.00)
b += item('Diplomatico', 5.00)
b += '\n' + EG
b += '\n' + ES

final = header + b + '\n' + footer

with open('D:/code/buns50/menu.html', 'w', encoding='utf-8') as f:
    f.write(final)

print("OK - chars:", len(final))
