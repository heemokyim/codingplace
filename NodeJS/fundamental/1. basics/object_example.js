// below is object literal syntax
var person={
    firstname:'Cloud',
    lastname:"Lee",
    greet: function(){
        console.log('hi '+this.firstname+this.lastname)
    }
}

// person can be accessed with dot operator
person.greet()

// or like dict() of python !
console.log(person['firstname'])