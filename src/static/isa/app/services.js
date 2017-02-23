'use strict';

app.factory('AuthenticationService', AuthenticationService);

app.factory('UserService', UserService);

app.factory('ProductService', ProductService);

app.factory('StoreService', StoreService);

app.factory('CountryService', CountryService);

app.factory('ProductCategoryService', ProductCategoryService);

app.factory('ShoppingCartService', ShoppingCartService);

app.factory('DostavljacService', DostavljacService);

app.factory('KupovinaService', KupovinaService);

app.factory('RecenzijaService', RecenzijaService);

app.factory('AkcijaService', AkcijaService);

app.factory('WishListService', WishListService);

app.factory('RecommendService', RecommendService);

function AuthenticationService($http, $cookieStore, $rootScope, $timeout, UserService) {
    var service = {};
    service.Login = Login;
    service.SetCredentials = SetCredentials;
    service.ClearCredentials = ClearCredentials;
    service.Auth = Auth;
    service.Logout = Logout;

    return service;

    function Login(user, callback) {
        /* Use this for real authentication
         ----------------------------------------------*/
        $http.post('rest/user/login', angular.toJson(user))
            .success(function (response) {
                callback(response);
            });

    }

    function Auth(callback) {
        $http.get('rest/user/authenticate').success(function (data) {
            callback(data);
        });
    }

    function Logout(callback) {
        $http.get('rest/user/logout').success(function (data) {
            callback(data);
        });
    }


    function SetCredentials(user) {

        //var authdata = Base64.encode(user.korisnickoime + ':' + user.lozinka);
        $rootScope.currentUser = user;
        //console.log($rootScope.currentUser);

        //$http.defaults.headers.common['Authorization'] = 'Basic ' + authdata; // jshint ignore:line
        //$cookieStore.put('globals', $rootScope.globals);

    }

    function ClearCredentials() {
        $rootScope.currentUser = null;
    }
}



function UserService($http) {
    var service = {};

    service.GetAll = GetAll;
    service.GetById = GetById;
    service.GetByUsername = GetByUsername;
    service.Create = Create;
    service.Update = Update;
    service.Delete = Delete;

    return service;

    function GetAll() {
        return $http.get('rest/user/get/all');
    }

    function GetById(id) {
        return $http.get('/api/users/' + id).then(handleSuccess, handleError('Error getting user by id'));
    }

    function GetByUsername(username) {
        return $http.get('/api/users/' + username).then(handleSuccess, handleError('Error getting user by username'));
    }

    function Create(user) {
        return $http.post('/api/users', user).then(handleSuccess, handleError('Error creating user'));
    }

    function Update(user) {
        return $http.put('rest/user/update', angular.toJson(user));
    }

    function Delete(id) {
        return $http.delete('/api/users/' + id).then(handleSuccess, handleError('Error deleting user'));
    }

    // private functions

    function handleSuccess(res) {
        return res.data;
    }

    function handleError(error) {
        return function () {
            return {
                success: false,
                message: error
            };
        };
    }
}

function ProductService($http) {
    
    var service = {};   
    
    service.create = create;
    service.update = update;
    service.remove = remove;
    service.addToCart = addToCart;
    service.getAll = getAll;
    service.getForUser = getForUser;
    
    return service;
    
    function getAll() {
        return $http.get('rest/product/get-all');
    }
    
    function getForUser() {
        return $http.get('rest/product/get-for-user');
    }
    
    function create(proizvod) {
        return $http.post('rest/product/add', angular.toJson(proizvod));
    }
    
    function update(proizvod) {
        return $http.put('rest/product/update', angular.toJson(proizvod));
    }
    
    function remove(proizvod) {
        console.log(proizvod);
        return $http.delete('rest/product/remove/' + proizvod.sifra);
    }
    
    function addToCart(product) {
        $http.get('rest/product/cart/add/' + product.sifra).success(function (data) {
            if(data) {
                $rootScope.cartCount = data;
            }
        });
    }
}

function StoreService($http) {
    var service = {};
    
    service.create = create;
    service.update = update;
    service.getAll = getAll;
    service.selectedProdavnica = {};
    
    return service;
    
    function create(prodavnica) {
        return $http.post('rest/prodavnica/add', angular.toJson(prodavnica));
    }
    
    function getAll() {
        return $http.get('rest/prodavnica/get/all');
    }
    
    function update(prodavnica) {
        return $http.put('rest/prodavnica/update', angular.toJson(prodavnica));
    }
}

function CountryService() {
    var service = {};
    service.allCountries = ['Srbija', 'Bosna', 'Hrvatska'];
    return service;
}

function ProductCategoryService($http) {
    var service = {};
    
    service.create = create;
    service.update = update;
    service.remove = remove;
    service.getAll = getAll;
    
    return service;
    
    function getAll() {
        return $http.get('rest/product/category/get-all');
    }
    
    function create(kat) {
        return $http.post('rest/product/category', angular.toJson(kat));
    }
    
    function update(kat) {
        return $http.put('rest/product/category', angular.toJson(kat));
    }
    
    function remove(kat) {
        return $http.delete('rest/product/category/delete/' + kat.naziv);
    }
}

function ShoppingCartService($http) {
    var service = {};
    
    service.getCartCount = getCartCount;
    service.getCartItems = getCartItems;
    service.removeCartItem = removeCartItem;
    service.buy = buy;
    
    return service;
    
    function getCartCount() {
        return $http.get('rest/product/cart');
    }
    
    function getCartItems() {
        return $http.get('rest/product/cart/get-all');
    }
    
    function removeCartItem(product) {
        return $http.delete('rest/product/cart/remove/' + product.sifra);
    }
    
    function buy(dostavljaci) {
        return $http.post('rest/product/cart/buy', angular.toJson(dostavljaci));
    }
}

function DostavljacService($http) {
    
    var service = {};
    
    service.create = create;
    service.update = update;
    service.remove = remove;
    service.getAll = getAll;
    
    return service;
    
    function getAll() {
        return $http.get('rest/product/dostavljac/get-all');
    }
    
    function create(dostavljac) {
        return $http.post('rest/product/dostavljac', angular.toJson(dostavljac));
    }
    
    function update(dostavljac) {
        return $http.put('rest/product/dostavljac', angular.toJson(dostavljac));
    }
    
    function remove(dostavljac) {
        return $http.delete('rest/product/dostavljac/' + dostavljac.sifra);
    }
}

function KupovinaService($http) {
    var service = {};
    
    service.remove = remove;
    service.getAll = getAll;
    service.createZalba = createZalba;
    service.getAllZalbe = getAllZalbe;
    service.odobriZalbu = odobriZalbu;
    
    return service;
    
    function getAll() {
        return $http.get('rest/product/kupovina/get-all');
    }
    
    function remove(dostavljac) {
        return $http.delete('rest/product/dostavljac/' + dostavljac.sifra);
    }
    
    function createZalba(zalba) {
        return $http.post('rest/product/zalba/add', angular.toJson(zalba));
    }
    
    function getAllZalbe() {
        return $http.get('rest/product/zalba/get-all');
    }
    
    function odobriZalbu(zalba) {
        return $http.delete('rest/product/zalba/confirm/' + zalba.sifra);
    }
}

function RecenzijaService($http) {
    var service = {};
    
    service.create = create;
    service.getAll = getAll;
    service.update = update;
    service.remove = remove;
    service.getRating = getRating;
    
    return service;
    
    function create(rec) {
        return $http.post('rest/product/recenzija/add', angular.toJson(rec));
    }
    
    function getAll(sifra) {
        return $http.get('rest/product/recenzija/get-all/' + sifra);
    }
    
    function update(rec) {
        return $http.put('rest/product/recenzija/update', angular.toJson(rec));
    }
    
    function remove(sifra) {
        return $http.delete('rest/product/recenzija/remove/' + sifra);
    } 
    
    function getRating(sifra) {
        return $http.get('rest/product/recenzija/rating/' + sifra);
    }
}

function AkcijaService($http) {
    
    var service = {};
    
    service.create = create;
    service.getAll = getAll;
    service.remove = remove;
    
    return service;
    
    function create(akcija) {
        return $http.post('rest/product/akcija/add', angular.toJson(akcija));
    }
    
    function getAll() {
        return $http.get('rest/product/akcija/get-all');
    }
    
    function remove(sifra) {
        return $http.delete('rest/product/akcija/' + sifra);
    }
    
    
    
}

function WishListService($http) {
    var service = {};
    
    service.create = create;
    service.getAll = getAll;
    service.checkAkcije = checkAkcije;
    
    return service;
    
    function create(proizvod) {
        zelja = {};
        zelja.proizvod = proizvod;
        return $http.post('rest/product/zelja/add', angular.toJson(zelja));
    }
    
    function getAll() {
        return $http.get('rest/product/zelja');
    }
    
    function checkAkcije() {
        return $http.get('rest/product/zelja/provera');
    }
}

function RecommendService($http) {
    
    var service = {};
    
    service.getProduct = getProduct;
    
    return service;
    
    function getProduct() {
        return $http.get("rest/product/recommend");
    }
}