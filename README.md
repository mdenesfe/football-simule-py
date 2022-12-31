# football-simule-py
This code appears to simulate a soccer match between two teams. It does this by reading in the team data from two text files, each containing a list of players with their respective attributes (name, age, number, position, attack, defense, midfield).

The code calculates the form factor for each player, which is a random value between 0 and 1. This value is used to scale the attack, defense, and midfield attributes of each player.

The code then calculates the attack, defense, and midfield attributes of each team by adding up the respective attributes of all the players on that team. It also applies an age factor to each player, which is a value between 0.7 and 1 that is based on the player's age. This age factor is used to further scale the attack, defense, and midfield attributes of each player.

Finally, the code calculates the score of the match by comparing the attack, defense, and midfield attributes of the two teams. It prints the final score of the match as well as the name of the winning team.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bu kod, iki takım arasında bir futbol maçını simüle etmeyi amaçlamaktadır. Bunu, iki adet metin dosyasından takım verilerini okuyarak yapar; her bir dosya, adı, yaşı, numarası, pozisyonu, saldırı, savunma ve orta saha özelliklerine sahip oyuncuların listesini içerir.

Kod, her oyuncu için bir form faktörü hesaplar, bu da 0 ile 1 arasında bir rastgele değerdir. Bu değer, her oyuncunun saldırı, savunma ve orta saha özelliklerini ölçeklendirmek için kullanılır.

Kod, her takımın saldırı, savunma ve orta saha özelliklerini, o takımdaki oyuncuların ilgili özelliklerini toplayarak hesaplar. Ayrıca, her oyuncuya bir yaş faktörü uygular, bu da 0.7 ile 1 arasında bir değerdir ve oyuncunun yaşına dayanır. Bu yaş faktörü, her oyuncunun saldırı, savunma ve orta saha özelliklerini daha da ölçeklendirmek için kullanılır.

Son olarak, kod, iki takımın saldırı, savunma ve orta saha özelliklerini karşılaştırarak maç skorunu hesaplar. Maçın son skorunu ve kazanan takımın adını yazdırır.
