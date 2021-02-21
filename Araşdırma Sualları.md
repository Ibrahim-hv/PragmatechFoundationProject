# Python araşdırma sualları və Cavabları

1. Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin:
    - İnterpreter proqramlaşdırma dili tərcüməçi kimi bilinir. Yəni proqram işlədikdə kodu maşın koduna çevirirlər. Bu dil, kodları sətir bə sətir oxuduğu üçün ilk səhvlə qarşılaşana qədər tərcümə etməyə davam edir. Səhvlə qarşılaşdığı zaman proqramı dayandırması, səhvi düzəltmək üçün aparılan analiz işini asanlaşdırır. İnterpreter dillər vasitəçi kod yaratmadığından, yaddaş baxımından olduqca səmərəlidirlər.

2. Interpreted və compiler dillər arasında olan fərqləri izah edin
    - İnterpreter dillər; ilk məlumatın həcmini ölçür, onun üçün lazım olan qədər yeri yaddaşda bron edir və ondan sonra bron etdiyi yerə dəyişənin adını verir.
    - Compiler dillərdə isə; nə qədər məlumat varsa, nə qədər yer tutacagın öncədən qeyd edilir, daha sonra məlumat yerləşdirilir.

3. Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin
    - Mətn növü: str -(Pythonda bir massiv kimdir və bir çox metodları var)
    - Rəqəmsal növlər: int -(tam +/- ədəd), float -(onluq +/- ədəd), complex -(mürəkkəb xəyali ədədlər)
    - Sıra növləri:
        - List: dəyişdirilə bilən bir massivdir. Təkrarlanan üzvlərə icazə verir.
        - Tuple: dəyişdirilməz bir massivdir. Təkrarlanan üzvlərə icazə verir.
        - Range: verilən başlanğıc ədədi ilə dayanma ədədi arasında dəyişməz rəqəmlər ardıcıllığını qaytarır.
    - Xəritəçəkmə növü:
        - Dict: sifariş edilmiş, sıralanmamış və dəyişdirilə bilən bir kolleksiyadır. Təkrarlanan üzv yoxdur.
    - Set növləri:
        - Set: sıralanmamış və indekssiz bir kolleksiyadır. Təkrarlanan üzv yoxdur.
        - Frozenset: verilmiş təkrarlanan elementlərdən başlanğıc edilən dəyişməz frozenset obyektini qaytarır.
    - Məntiq növü: bool -(iki dəyərdən birini təmsil edir: True ya False)
    - İkili növlər: bytes, bytearray, memoryview
4. Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin
    - OOP kompüter proqramları və tətbiqləri yaratmaq üçün proqramlaşdırma paradiqmasıdır.
    - Bu paradiqma, funksiyalar və məntiq deyil, məlumatlar və ya obyektlər ətrafında proqram dizaynını təşkil edən bir kompüter proqramlaşdırma modelidir.

5. Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?
    - Bildiyim qədəri ilə, metod hər hansı sinfə (CLASS), yaxud obyektə aid olan funksiya və ya prosedur. Bunu əsas tutaraq deyə bilərəm ki, sinifin içinə funksiya yazarkən metod istifadə etdmiş və ya yaratmış oluruq.

6. Local və Global variable nədir izah edin
    - Burada müəllimin çəkmiş olduğu Respublika, Muxtar Respublika misalını göstərmək olar.
    Bundan əlavə olaraq Python -da "global" açar sözü var ki, bundan istifadə edərək Local-da (funksia daxilində) olan dəyişəni qlobal etmək mümkündür.

7. Python type conversion haqqında izahat verin
    - Type Conversion -un 2ci adı da Type Castingdir ki, daxil olan hər hansı 1 məlumatın digər məlumat növünə çevrilməsidir.

8. İnit nədir?
    - Bütün siniflər __init__ () adlı bir funksiyaya malikdir. __İnit__ () funksiyasından istifadə edərək obyekt xüsusiyyətlərinə dəyərlər təyin etmək olur.

9. Self nədir?
    - Self parametri, class-a aid olmayan, class-a aid dəyişənlərə daxil olmaq üçün istifadə olunan və bunun üçündə sinifdəki hər hansı bir funksiyanın ilk parametridir.

10. *args,*kwargs nədir? nə zaman istifadə olunur?
    - *args Arqument sözünün qıssaldılmış variantıdır. Nə qədər arqument veriləcəyi bilinmirsə, funksiya tərifində parametr adından əvvəl* əlavə edilir.
    - *kwargs Keyword Arqument sözünün qıssaldılmış variantıdır. Nə qədər açar söz arqumentinin veriləcəyi bilinmirsə, funksiya tərifindəki parametr adından əvvəl ** əlavə edilir.

11. Python module nədir?
    - Modul kod kitabxanası kimidir. Tətbiqə daxil etmək istədiyimiz bir sıra funksiyaları ehtiva edən bir sənəddir. Bir modul yaratmaq üçün istədiyimiz kodu fayl uzantısı .py olan bir faylda saxlamağımız kifayətdir. Python'da istədiyimiz zaman idxal edə biləcəyimiz bir neçə daxili modul var: platform, dir(), from.

12. Python package nədir?
    - PIP: Python paketləri və ya modullar üçün paket meneceridir. Paket bir modul üçün lazım olan bütün sənədləri ehtiva edir.

13. pass nədir? Nə zaman istifadə olunur?
    - PASS gələcək kod üçün yer tutucu kimi istifadə olunur. PASS icra edildikdə heç bir şey olmur. loop -larda, function və class definition -larda, eləcə də if -lərdə istifadə etməyə icazə verilmir.

14. List metodlarından 5 ədəd metodun izahatını yazın
    - append () Siyahının sonuna bir element əlavə edir
    - clear () Bütün elementləri siyahıdan çıxarır
    - sort () Siyahını sıralayır
    - count () Müəyyən olunmuş dəyərə malik elementlərin sayını qaytarır
    - pop () Elementi göstərilən mövqedən silir

15. List və dict hansı hallarda istifadə olunur?
    - List birdən çox maddəni bir dəyişəndə ​​saxlamaq üçün istifadə olunur. Dict isə məlumat dəyərlərini (key: value) saxlamaq üçün istifadə olunur. Bundan əlavə Dict sifariş edilmiş, dəyişdirilə bilən və təkrarlanmağa icazə verilməyən bir kolleksiyadır.
    Hər hansı məlumatları siyahıya almaq istədiyimizdə LİST, onların (və ya başqa halda) dəyərlər saxlamasını istədiyimizdə DİCT istifadə edə bilərik.

16. Dict metodlarından 5 ədəd metodun izahatını yazın
    - clear () Dict daxilindəki bütün elementləri silir
    - copy () Dict -in surətini qaytarır
    - get () Göstərilən açarın (key) dəyərini qaytarır
    - pop () Göstərilən açar ilə elementi (value) silir
    - values () Dict -dəki bütün dəyərlərin siyahısını qaytarır
