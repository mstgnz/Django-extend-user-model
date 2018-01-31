# Custom user model for Django Framework

> Django'nun kullanıcı modelini genişletmek ve orjinal modelden tek farkının ekstra alanlar 
> ve e-mail ile giriş yapmak ise doğru yerdesiniz.

* İlk önce 'account' adında bir uygulama oluşturuyoruz. Siz farklı isimde verebilirsiniz. Terminalden;

`python3 manage.py startapp account`
* Oluşturduğunuz 'account' uygulamasının admin.py ve models.py dosyalarının içeriğini yukarıdan kopyalabilirsiniz.
* 'account' uygulamasının settings.py dosyasında ki ayarlarını yapıyoruz.
* INSTALLED_APPS bölümüne oluşturduğumuz uygulamayı yazıyoruz.

`INSTALLED_APPS = [
    ....
    'account',
]`
* Settings.py dosyasında User modelimizi tanıtmamız gerekiyor. Bunun için de herhangi bir yere aşağıda ki kodu yapıştırınız.

`AUTH_USER_MODEL = 'account.User'`
* Terminal ekranından artık uygulamayı hayata geçirebiliriz. Sırasıyla;

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

`email : blablabla@blabla.com`

`password : 123456`

`python3 manage.py runserver`

>Admin paneline giri yaptığınızda orjinal django user modelinden tek 
>farkının girdiğiniz ekstra alanlar ve email sistemi ile giriş olduğunu göreceksiniz.
