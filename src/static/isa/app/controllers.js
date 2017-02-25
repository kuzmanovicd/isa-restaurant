'use strict';

app.controller('UserController', function ($scope, UserService) {
    $scope.UserService = UserService;

    UserService.GetAll().success(function (data) {
        $scope.users = data;
    });


    $scope.edit = function (user) {
        console.log("EDIT USER");
        UserService.editUser = {};
        angular.copy(user, UserService.editUser);
    };

    $scope.submit = function (user) {
        UserService.Update(user).success(function (data) {

            UserService.GetAll().success(function (data) {
                $scope.users = data;
            });
        });
    }

});

app.controller('loginController', function ($scope, $location, $rootScope, $cookieStore, AuthenticationService) {

    $scope.loginsubmit = login;
    
    function login() {
        $scope.dataLoading = true;
        AuthenticationService.Login($scope.user, function (data) {
            if (data.user.username) {
                AuthenticationService.SetCredentials(data);
                $location.path('/');
            } else {
                // FlashService.Error(response.message);
                $scope.dataLoading = false;
            }
        });
    }
});



app.controller('productsController', function ($scope, $rootScope, $http, $location, $timeout, Upload, ProductService, ProductCategoryService, StoreService, RecenzijaService, WishListService) {

    $scope.pr = ProductService;

    if ($location.path() == '/proizvod' && !$scope.pr.selectedProduct) {
        $location.path('/proizvodi');
    }

    if ($location.path() == '/proizvod') {
        loadRecenzije();
    }

    ProductCategoryService.getAll().success(function (data) {
        $scope.categories = data;
    });

    StoreService.getAll().success(function (data) {
        $scope.stores = data;
        $scope.storesDownloaded = true;
    });


    ProductService.getAll().success(function (data) {
        $scope.products = data;
    });

    $scope.getStoreName = function (sifra) {
        if (!$scope.storesDownloaded) {
            return;
        }
        for (var i = 0; i < $scope.stores.length; i++) {
            if ($scope.stores[i].sifra == sifra) {
                return $scope.stores[i].naziv;
            }
        }
    };

    $scope.isAllowed = function (p) {

        if ($rootScope.currentUser.role == 'ADMIN') {
            return true;
        } else if ($rootScope.currentUser.role == 'BUYER') {
            return false;
        }

        if (!$scope.stores) {
            return false;
        }

        for (var i = 0; i < $scope.stores.length; i++) {
            if ($scope.stores[i].sifra == p.prodavnica) {
                if ($scope.stores[i].odgovorniProdavac == $rootScope.currentUser.username) {
                    return true;
                }
            }
        }
        return false;
    };

    $scope.proizvod = {};

    $scope.create = function (proizvod) {

        uploadImages();
        uploadVideo(addProduct);

        function addProduct() {
            ProductService.create(proizvod).success(function (data) {
                console.log('test: ' + data);
                if (data) {
                    $scope.failure = false;
                    $location.path('/proizvodi');
                } else {
                    $scope.failure = true;
                }

            });
            console.log("KRAJ DODAVANJA");
        }
    };

    $scope.update = function (proizvod) {
        $scope.proizvod = proizvod;

        if ($scope.izmeniSlike) {
            uploadImages();
            uploadVideo(changeProduct);
        } else {
            changeProduct();
        }

        function changeProduct() {
            ProductService.update(proizvod).success(function (data) {
                if (data) {
                    $scope.failure = false;
                    $location.path('/proizvodi');
                } else {
                    $scope.failure = true;
                }

            });
            console.log("KRAJ DODAVANJA");
        }
    }

    $scope.remove = function (proizvod) {
        var isConfirmed = confirm("Da li ste sigurni da zelite da obrisete " + proizvod.naziv + "?");
        if (isConfirmed) {
            ProductService.remove(proizvod).success(function (data) {
                if (data) {
                    $location.path('/proizvodi')
                }
            });
        }
    }

    $scope.selectProduct = function (product) {
        $scope.pr.selectedProduct = product;
        console.log($scope.pr.selectedProduct);
    };

    $scope.edit = function (product) {
        ProductService.selectedProduct = product;
        $location.path('proizvod/izmena')
    };

    $scope.addToCart = function (product) {
        $http.get('rest/product/cart/add/' + product.sifra).success(function (data) {
            if (data) {
                $rootScope.cartCount = data;
            }
        });
    };

    //UPLOAD
    function uploadVideo(callback) {
        var file = $scope.videoFile;
        //console.log(file);
        $scope.proizvod.video = {};
        $scope.videoFiles = [];
        $scope.videoFiles.push(file);
        file.upload = Upload.upload({
            url: 'rest/product/upload',
            data: {
                file: file
            }
        });

        file.upload.then(function (response) {
            $timeout(function () {
                $scope.proizvod.video = response.data;
                file.result = response.data;
                callback();
            });
        }, function (response) {
            if (response.status > 0) {
                $scope.errorMsg = response.status + ': ' + response.data;
            }
        }, function (evt) {
            file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
        });

    }

    function uploadImages() {
        $scope.proizvod.slika = [];
        $scope.files = $scope.imageFiles; //files;
        //$scope.errFiles = errFiles;
        angular.forEach($scope.files, function (file) {
            file.upload = Upload.upload({
                url: 'rest/product/upload',
                data: {
                    file: file
                }
            });

            file.upload.then(function (response) {
                $timeout(function () {
                    $scope.proizvod.slika.push(response.data);
                    file.result = response.data;
                    //callback();
                });
            }, function (response) {
                if (response.status > 0) {
                    $scope.errorMsg = response.status + ': ' + response.data;
                }
            }, function (evt) {
                file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
            });
        });
    }

    //Recenzije
    $scope.createRecenzija = function (rec) {
        rec.sifra = $scope.pr.selectedProduct.sifra;

        RecenzijaService.create(rec).success(function (data) {
            if (data) {
                loadRecenzije();
            }
        });

        $scope.rec = {};

    };

    $scope.editRecenzija = function (rec) {
        RecenzijaService.selectedRecenzija = rec;
        $location.path('/recenzija/izmena');
    };

    $scope.removeRecenzija = function (rec) {
        RecenzijaService.remove(rec.sifra).success(function (data) {
            if (data) {
                loadRecenzije();
            }
        });
    };

    function loadRecenzije() {
        RecenzijaService.getAll($scope.pr.selectedProduct.sifra).success(function (data) {
            if (data) {
                $scope.recenzije = data;
            }
        });

        RecenzijaService.getRating($scope.pr.selectedProduct.sifra).success(function (data) {
            if (data) {
                $scope.prosecnaOcena = data;
            }
        });
    }
    
    //wish list
    $scope.addToWishList = function(proizvod) {
        WishListService.create(proizvod).success(function(data) {
            //
        });
    }

});

app.controller('RecenzijaController', function ($scope, $location, RecenzijaService) {
    $scope.selectedRecenzija = RecenzijaService.selectedRecenzija;
    $scope.update = function (rec) {
        RecenzijaService.update(rec).success(function (data) {
            if (data) {
                $location.path('/proizvodi');
            }
        });
    };
});

app.controller('StoreController', function ($scope, $location, $timeout, StoreService, UserService, CountryService) {

    UserService.GetAll().success(function (data) {
        $scope.users = data;
    });

    StoreService.getAll().success(function (data) {
        $scope.stores = data;
    });

    $scope.prodavnica = {};

    $scope.selectedProdavnica = StoreService.selectedProdavnica;

    $scope.allCountries = CountryService.allCountries;

    $scope.create = function (prod) {
        console.log(prod);

        StoreService.create(prod).success(function (data) {
            console.log('test: ' + data);
            if (data) {
                $scope.failure = false;
                $location.path('/prodavnice');
            } else {
                $scope.failure = true;
            }

        });

    };

    $scope.update = function (prod) {
        StoreService.update(prod).success(function (data) {
            if (data) {
                $scope.failure = false;
                $location.path('/prodavnice');
            } else {
                $scole.failure = true;
            }
        });
    }

    $scope.editStore = function (store) {
        StoreService.selectedProdavnica = store;
        $location.path('/prodavnica/izmena');
    };
});



app.controller('ShoppingCartController', function ($scope, $rootScope, ShoppingCartService, DostavljacService) {

    $scope.ShoppingCartService = ShoppingCartService;

    DostavljacService.getAll().success(function (data) {
        $scope.dostavljaci = data;
    });

    $scope.cenaDostave = [];
    $scope.sifreDostavljaca = [];

    /*
    $scope.ukupnaCenaDostave = function() {
        var ukupno = 0;
        for(var i = 0; i < $scope.cenaDostave.length; i++) {
            ukupno += Number($scope.cenaDostave[i]);
        }
        return ukupno;
    };
    */
    $scope.ukupnaCenaDostave = function () {
        var ukupno = 0;
        for (var i = 0; i < $scope.sifreDostavljaca.length; i++) {
            for (var j = 0; j < $scope.dostavljaci.length; j++) {
                if ($scope.dostavljaci[j].sifra == $scope.sifreDostavljaca[i]) {

                    if (!$scope.cart.stores) {
                        return 0;
                    }

                    $scope.cenaDostave[i] = $scope.dostavljaci[j].tarifa * $scope.cart.deliveryPrice[$scope.cart.stores[i].sifra];
                    ukupno += $scope.cenaDostave[i];
                }
            }
        }
        return ukupno;
    };

    ShoppingCartService.getCartItems().success(function (data) {
        if (data) {
            $scope.cart = data;
            $rootScope.cartCount = data.items.length;
        }
    });

    $scope.remove = function (product) {
        ShoppingCartService.removeCartItem(product).success(function (data) {
            if (data) {
                $scope.cart = data;
                $rootScope.cartCount = data.items.length;
                $scope.cenaDostave = [];
            }
        });
    }

    $scope.ifCanDeliver = function (dostavljac, store) {
        var okayUser = false;
        var okayStore = false;
        for (var i = 0; i < dostavljac.drzave.length; i++) {
            if ($rootScope.currentUser.drzava == dostavljac.drzave[i]) {
                okayUser = true;
                break;
            }
        }

        for (var i = 0; i < dostavljac.drzave.length; i++) {
            if (store.drzava == dostavljac.drzave[i]) {
                okayStore = true;
                break;
            }
        }

        return okayUser && okayStore;

    };

    $scope.buy = function () {
        ShoppingCartService.buy($scope.sifreDostavljaca).success(function (data) {
            if (data) {
                $scope.cart = data;
                $rootScope.cartCount = data.items.length;
            }
        });
    };

});

app.controller('KupovinaController', function ($scope, $location, $rootScope, KupovinaService) {

    KupovinaService.getAll().success(function (data) {
        $scope.kupovine = data;
    });

    $scope.selectedKupovina = KupovinaService.selectedKupovina;

    $scope.z = {};

    $scope.zalba = function (kupovina) {
        KupovinaService.selectedKupovina = kupovina;
        $location.path('/zalba');
    }

    $scope.allowedZalba = function (kupovina) {
        var d = new Date();
        var mil = 1000 * 60 * 60 * 24;
        //mil = 1000000;

        if ((d.getTime() - kupovina.vreme - kupovina.trajanjePrenosa * mil) > (7 + kupovina.trajanjePrenosa) * mil) {
            return false;
        } else {
            return true;
        }

    };

    $scope.createZalba = function (z) {
        if (!$scope.selectedKupovina) {
            return;
        }

        z.sifra = $scope.selectedKupovina.sifra;
        z.kupac = $rootScope.currentUser.username;
        z.prodavnica = $scope.selectedKupovina.prodavnica;

        //console.log(z);
        KupovinaService.createZalba(z).success(function (data) {
            if (data) {
                $scope.failure = false;
                $location.path('/istorijakupovine')
            } else {
                $scope.failure = true;
            }
        });
    };
});

app.controller('ZalbeController', function ($scope, KupovinaService) {
    getAll();

    $scope.odobri = function (z) {
        KupovinaService.odobriZalbu(z).success(function (data) {
            getAll();
        });
    };

    function getAll() {
        KupovinaService.getAllZalbe().success(function (data) {
            $scope.zalbe = data;
        });
    }
});

app.controller('logoutController', function ($scope, $location, $rootScope, AuthenticationService) {
    $scope.logout = logout;

    function logout() {
        AuthenticationService.ClearCredentials();
        AuthenticationService.Logout(function (data) {
            $location.path("/");
        });

        // $rootScope.loggedIn = false;
    }
});

app.controller('registerController', function ($scope, $http, $location, CountryService) {
    $scope.allCountries = CountryService.allCountries;

    $scope.registersubmit = function () {
        console.log(angular.toJson($scope.user));
        if (!$scope.user.tip) {
            $scope.user.tip = 'kupac';
        }

        $http.post('rest/user/register', angular.toJson($scope.user)).success(function (data) {
            if (data.success == true) {
                $location.path('/');
            }
        });
    }
});


app.controller('ProductCategoryController', function ($scope, $location, ProductCategoryService) {

    getAll();

    $scope.selectedKategorija = ProductCategoryService.selectedKategorija;

    $scope.create = function (kat) {
        ProductCategoryService.create(kat).success(function (data) {
            if (data) {
                $scope.failure = false;
                getAll();
                $location.path('/');
            } else {
                $scope.failure = true;
            }
        });
    }

    $scope.update = function (prod) {
        ProductCategoryService.update(prod).success(function (data) {
            if (data) {
                $scope.failure = false;
                getAll();
                $location.path('/');
            } else {
                $scole.failure = true;
            }
        });
    }

    $scope.editCategory = function (category) {
        ProductCategoryService.selectedKategorija = category;
        $location.path('/kategorija/izmena');
    };

    $scope.remove = function (kat) {
        var isConfirmed = confirm("Da li ste sigurni da zelite da obrisete " + kat.naziv + "?");
        if (isConfirmed) {
            ProductCategoryService.remove(kat).success(function (data) {
                getAll();
            });
        }

    }

    function getAll() {
        ProductCategoryService.getAll().success(function (data) {
            $scope.categories = data;
        });
    }
});

app.controller('DostavljacController', function ($scope, $location, DostavljacService, CountryService) {
    $scope.allCountries = CountryService.allCountries;
    getAll();
    $scope.selectedDostavljac = DostavljacService.selectedDostavljac;

    $scope.create = function (dostavljac) {
        DostavljacService.create(dostavljac).success(function (data) {
            if (data) {
                getAll();
                $location.path('/admin');
            }
        });
    }

    $scope.update = function (dostavljac) {
        DostavljacService.update(dostavljac).success(function (data) {
            if (data) {
                getAll();
                $location.path('/admin');
            }
        });
    }

    $scope.remove = function (dostavljac) {
        var isConfirmed = confirm("Da li ste sigurni da zelite da obrisete " + dostavljac.naziv + "?");
        if (isConfirmed) {
            DostavljacService.remove(dostavljac).success(function (data) {
                if (data) {
                    getAll();
                    $location.path('/admin');
                }
            });
        }
    }

    $scope.edit = function (dostavljac) {
        DostavljacService.selectedDostavljac = dostavljac;
        $location.path('/dostavljac/izmena');
    };

    function getAll() {
        DostavljacService.getAll().success(function (data) {
            $scope.dostavljaci = data;
        });
    }
});

app.controller('AkcijaController', function ($scope, $rootScope, $location, ProductService, AkcijaService) {
    $scope.akcija = {};
    $scope.todayDate = new Date();
    $scope.date = "";
    
    getAll();
    
    $scope.getProizvodCena = function (sifra) {
        for(var i = 0; i < $scope.products.length; i++) {
            if($scope.products[i].sifra == sifra) {
                return $scope.products[i].jedinicnaCena;
            }
        }
    };
    
    ProductService.getForUser().success(function (data) {
        $scope.products = data;
    });

    $scope.do = function () {
        $scope.akcija.datumZavrsetka = Date.parse($scope.date)
    };
    
    $scope.create = function(akcija) {
        AkcijaService.create(akcija).success(function(data) {
            if(data) {
                getAll();
                $location.path('/proizvodi');
            }
        });
    };
    
    $scope.remove = function(akcija) {
        AkcijaService.remove(akcija.proizvod).success(function(data) {
            if(data) {
                getAll();
            }
        });
    };
    
    $scope.allowed = function (a) {
        var d = new Date();
        var mil = 1000 * 60 * 60 * 24;
        //mil = 1000000;

        if (d.getTime() > a.datumZavrsetka) {
            return false;
        } else {
            return true;
        }

    };
    
    function getAll() {
        AkcijaService.getAll().success(function(data) {
            if(data) {
                $scope.akcije = data;
            }
        });
    }

});

app.controller('WishListController', function($scope, WishListService) {
    WishListService.getAll().success(function(data) {
        $scope.listazelja = data;
    });
    
    WishListService.checkAkcije().success(function(data) {
        $scope.wishlist = data;
    });
});

app.controller('RecommendController', function($scope, $location, $rootScope, ProductService, RecommendService) {
    $scope.allowedToShow = function() {
        if(!$rootScope.currentUser) {
            return false;
        }
        //console.log($location.path() + '  :  ' + $rootScope.currentUser.role)
        if($location.path() == '/home' && $rootScope.currentUser.role == 'BUYER') {
            return true;
        } else {
            return false;
        }
    };
    
    RecommendService.getProduct().success(function(data) {
        if(data) {
            $scope.proizvod = data;
        }
    });
    
    $scope.buy = function (proizvod) {
        ProductService.selectedProduct = proizvod;
        $location.path('/proizvod');
    };
});