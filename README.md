# number_game

# GUESS GAME
Guess game sadə terminal oyunudur. İstifadəçidən rəqəm soruşursuz o isə tapır. 
Sonsuz sayda turları uzada bilərsiniz. Hər turda 5 qərəm olacaq, hər rəqəmi tapması üçün istifadəçiyə 5 cəhd şansı verirsiniz. Daha ətraflı desək - Siz xəyalınızda bir rəqəm tutursunuz və istifadəçiyə onu tapmağı əmr edirsiniz. Lakin istifadəçinin 5 cəhdi var. Hər cəhddə siz ona ipucları ilə kömək etməlisiniz. Misalçün - sənin dediyin rəqəm böyükdür... amma indi kiçikdir... yaxınlaşırsan amma yenə kiçikdir... və s. Birinci rəqəm tapıldıqda istifadəçinin xallarına +1 əlavə edirsiniz. Sonra növbəti rəqəmə keçirsiniz və s.

## Prerequisites
* inquirer modulundan istifadə edin

## Qaydalar
- itertools modulundan istifadə edərək sonsuz döngü yaratmalıdır.
- Hər döngüdə 5 elementli generator yaratmalıdır. Hər bir elementi 1-dən 100-ə qədər rəqəmlər olmalıdır
- İstifadəçiyə bu barədə xəbərdarlıq edilməlidir ki, sizi qarşıda 5 oyun gözləyir + istifadəçinin cari xalı. Davam etmək istədiyini soruşun.
- Əgər davam etmək istəyirsə onda ilk rəqəmi generatordan çəkin, lakin onu istifadəçiyə göstərmədən təsadüfi bir rəqəm daxil etməsini istəyin. Bu rəqəmi gizlətdiyiniz rəqəmlə müqayisə edərək istifadəçiyə köməklik göstərin.
- Əgər 5 cəhdin heç birisini dəyərləndirə bilməsə onda cari rəqəm üçün onu uduzmuş sayın və keçin növbəti rəqəmə. Əks təqdirdə növbəti rəqəmə keçməzdən əvvəl istifadəçinin xalını +1 qədər artırın.
- Cari turdakı 5 rəqəmin hamısı bitdikdə, istifadəçiyə onun xallarını göstərin və növbəti mərhələyə keçib keçmək istəmədiyini soruşun. Əgər istifadəçi hə desə sonsuz döngünün ikinci addımına keçmiş olassınız.
- Əgər istifadə növbəti tura keçmək istəmirsə onda oyunu dayandırın və proqramdan çıxın.
