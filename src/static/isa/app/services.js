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

function AuthenticationService($http, $cookies, $rootScope, $timeout, UserService) {
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
        console.log(angular.toJson(user));
        $http.post('api/users/auth/', angular.toJson(user))
            .success(function (response) {
                callback(response);
            });
    }

    function Auth(token, callback) {
        $http.post('api/users/verify/', angular.toJson(token)).success(function (data) {
            callback(data);
        });
    }

    function Logout(callback) {
        $http.get('api/users/logout').success(function (data) {
            callback(data);
        });
    }


    function SetCredentials(data) {
        $rootScope.currentUser = data.user;
        $http.defaults.headers.common['Authorization'] = 'JWT ' + data.token;
        $cookies.put('token', data.token);
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
        return $http.get('api/users/get/all');
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
        return $http.put('api/users/update', angular.toJson(user));
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
        return $http.get('api/product/get-all');
    }
    
    function getForUser() {
        return $http.get('api/product/get-for-user');
    }
    
    function create(proizvod) {
        return $http.post('api/product/add', angular.toJson(proizvod));
    }
    
    function update(proizvod) {
        return $http.put('api/product/update', angular.toJson(proizvod));
    }
    
    function remove(proizvod) {
        console.log(proizvod);
        return $http.delete('api/product/remove/' + proizvod.sifra);
    }
    
    function addToCart(product) {
        $http.get('api/product/cart/add/' + product.sifra).success(function (data) {
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
        return $http.post('api/prodavnica/add', angular.toJson(prodavnica));
    }
    
    function getAll() {
        return $http.get('api/prodavnica/get/all');
    }
    
    function update(prodavnica) {
        return $http.put('api/prodavnica/update', angular.toJson(prodavnica));
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
        return $http.get('api/product/category/get-all');
    }
    
    function create(kat) {
        return $http.post('api/product/category', angular.toJson(kat));
    }
    
    function update(kat) {
        return $http.put('api/product/category', angular.toJson(kat));
    }
    
    function remove(kat) {
        return $http.delete('api/product/category/delete/' + kat.naziv);
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
        return $http.get('api/product/cart');
    }
    
    function getCartItems() {
        return $http.get('api/product/cart/get-all');
    }
    
    function removeCartItem(product) {
        return $http.delete('api/product/cart/remove/' + product.sifra);
    }
    
    function buy(dostavljaci) {
        return $http.post('api/product/cart/buy', angular.toJson(dostavljaci));
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
        return $http.get('api/product/dostavljac/get-all');
    }
    
    function create(dostavljac) {
        return $http.post('api/product/dostavljac', angular.toJson(dostavljac));
    }
    
    function update(dostavljac) {
        return $http.put('api/product/dostavljac', angular.toJson(dostavljac));
    }
    
    function remove(dostavljac) {
        return $http.delete('api/product/dostavljac/' + dostavljac.sifra);
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
        return $http.get('api/product/kupovina/get-all');
    }
    
    function remove(dostavljac) {
        return $http.delete('api/product/dostavljac/' + dostavljac.sifra);
    }
    
    function createZalba(zalba) {
        return $http.post('api/product/zalba/add', angular.toJson(zalba));
    }
    
    function getAllZalbe() {
        return $http.get('api/product/zalba/get-all');
    }
    
    function odobriZalbu(zalba) {
        return $http.delete('api/product/zalba/confirm/' + zalba.sifra);
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
        return $http.post('api/product/recenzija/add', angular.toJson(rec));
    }
    
    function getAll(sifra) {
        return $http.get('api/product/recenzija/get-all/' + sifra);
    }
    
    function update(rec) {
        return $http.put('api/product/recenzija/update', angular.toJson(rec));
    }
    
    function remove(sifra) {
        return $http.delete('api/product/recenzija/remove/' + sifra);
    } 
    
    function getRating(sifra) {
        return $http.get('api/product/recenzija/rating/' + sifra);
    }
}

function AkcijaService($http) {
    
    var service = {};
    
    service.create = create;
    service.getAll = getAll;
    service.remove = remove;
    
    return service;
    
    function create(akcija) {
        return $http.post('api/product/akcija/add', angular.toJson(akcija));
    }
    
    function getAll() {
        return $http.get('api/product/akcija/get-all');
    }
    
    function remove(sifra) {
        return $http.delete('api/product/akcija/' + sifra);
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
        return $http.post('api/product/zelja/add', angular.toJson(zelja));
    }
    
    function getAll() {
        return $http.get('api/product/zelja');
    }
    
    function checkAkcije() {
        return $http.get('api/product/zelja/provera');
    }
}

function RecommendService($http) {
    
    var service = {};
    
    service.getProduct = getProduct;
    
    return service;
    
    function getProduct() {
        return $http.get("api/product/recommend");
    }
}