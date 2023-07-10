<h1 align="center">Firebase API Example</h1>

<br>

Bu proje, Python Flask kütüphanesini kullanarak Firebase veritabanına erişim sağlayan bir API geliştirmeyi amaçlar. Firebase, kullanıcıların gerçek zamanlı verileri depolamalarına, senkronize etmelerine ve paylaşmalarına olanak tanıyan bir bulut tabanlı veritabanıdır. API, kullanıcılara veri ekleme, görüntüleme ve silme işlemlerini gerçekleştirme yeteneği sunar.

<br>

## Proje'nin Özellikleri:

-   Veri tabanında ki verileri okuyabilirsiniz
-   Veri tabanına JSON formatından veri ekleyebilirsiniz
-   Veri tabanında ki tabloları görüntüleyebilirsiniz.
-   Veri tabanında ki tabloları silebilirsiniz.

<br>

## Proje de Kullanılan Kütüphaneler;

-   ### [Firebase](https://pypi.org/project/firebase-admin/)

-   ### [Flask](https://pypi.org/project/Flask/)

<br>

## Proje'yi İndirme

```shell
git clone REPO_URL
cd firebase-api
```

## Kurulum

Firebase'den proje oluşturduktan sonra, `Project settings` sekmesindenden service accounts dan Python'ı seçip **Generate new private key** butonuna basıp API bilgilerini indirin, indirdikten sonra ismini **key.json** yapıp **firebase/api** klasörüne attın.

<hr>

### Gerekli kütüphanelerini kurulumu ve projeyi çalıştırma

```shell
pip install -r requirements.txt
# Gerekli kütüphanelerini kurulumu
python main.py
# main.py dosyasını çalıştırır.
```

### Veri tabanında ki verileri görüntüleme, veri ekleme ve silme

<hr>

Verileri görüntülemek için aşağıda ki URL'e GET istediği atmanız yeterli.

```shell
http://127.0.0.1:5000/user/list
```

**Example**

![image](/images/example2.png)

<hr>

Veri tabanına veri ekleme için ise aşağıda ki URL'e eklemek istediğiniz veri ile POST istediği atmanız yeterli.

```shell
http://127.0.0.1:5000/user/add
```

**Example**

![image](/images/example1.png)

<hr>

Veri tabanında ki document görüntülemek için aşağıda ki URL'e GET istediği atmanız yeterli.

```shell
http://127.0.0.1:5000/user/doclist
```

**Example**

![image](/images/example3.png)

<hr>

Veri tabanından document silmek için aşağıda ki URL'e DELETE istediği atmanız yeterli.

```shell
http://127.0.0.1:5000/user/delete/<document_id>
```

**Example**

![image](/images/example4.png)

<hr>
