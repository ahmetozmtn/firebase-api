<h1 id="tr" align="center">Firebase API Example</h1>

<h2 align="center"> <a href="#tr">Turkish</a> | <a href="#eng">English</a>  </h2>

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

Lütfen yukarıdaki URL'lerin, projeyi makinenizde yerel olarak çalıştırdığınızı varsaydığını unutmayın. Projeyi farklı bir sunucuda veya bağlantı noktasında çalıştırıyorsanız, temel URL'yi uygun şekilde değiştirin.

<hr>

<h1 id="eng" align="center">Firebase API Example</h1>

<br>

This project aims to develop an API that accesses the Firebase database using the Python Flask library. Firebase is a cloud-based database that allows users to store, synchronize, and share real-time data. The API provides users with the ability to add, view, and delete data.

<br>

## Features of the Project:

-   Ability to read data from the database
-   Ability to add data to the database in JSON format
-   Ability to view tables in the database
-   Ability to delete tables in the database

<br>

## Libraries Used in the Project:

-   ### [Firebase](https://pypi.org/project/firebase-admin/)

-   ### [Flask](https://pypi.org/project/Flask/)

<br>

## Project Setup

```shell
git clone REPO_URL
cd firebase-api
```

## Installation

After creating a project on Firebase, go to the `Project settings` tab, select Python from the service accounts, and click the **Generate new private key** button to download the API credentials. Rename the downloaded file to **key.json** and place it in the **firebase/api** folder.

<hr>

### Installing the required libraries and running the project

```shell
pip install -r requirements.txt
# Install the required libraries
python main.py
# Run the main.py file
```

### Viewing, Adding, and Deleting Data in the Database

<hr>

To view the data in the database, simply send a GET request to the following URL:

```shell
http://127.0.0.1:5000/user/list
```

**Example**

![image](/images/example2.png)

<hr>

To add data to the database, send a POST request to the following URL with the data you want to add:

```shell
http://127.0.0.1:5000/user/add
```

**Example**

![image](/images/example1.png)

To view the documents in the database, send a GET request to the following URL:

```shell
http://127.0.0.1:5000/user/doclist
```

**Example**

![image](/images/example3.png)

To delete a document from the database, send a DELETE request to the following URL with the document ID:

```shell
http://127.0.0.1:5000/user/delete/<document_id>
```

**Example**

![image](/images/example4.png)

<hr>

Please note that the above URLs assume you are running the project locally on your machine. Modify the base URL accordingly if you are running the project on a different server or port.

