"use strict"

class Vehicle
{
    #privateMember;
    publicMember;
    static staticMember = 'I am a public static member.'
    static #privateStaticMember = 'I am a private static member.'

    constructor() {
        //console.log('Setting member property')
        //this.#privateMember = 'I am a private member.'
        this.myPrivateMember = 'I am a private member.'
        this.publicMember = 'I am a public member'
        //console.log('Member properties are all set')
    }

    publicMethod() {
        console.log("Public method called!")
    }

    _privateMethod() {
        console.log("Private method called!")
    }

    static publicMethod() {
        console.log("Public static method called!")
    }

    static _privateMethod() {
        console.log("Private static method called!")
    }

    get myPrivateMember()
    {
        return this.#privateMember
    }
    
    set myPrivateMember(val) {
        this.#privateMember = val
    }

}

class TwoWheeler extends Vehicle
{
    noOfWheel
    constructor() {
        super()
        this.noOfWheel = 2
    }

    getWheelCount()
    {
        return this.noOfWheel
    }
}

//let obj = new Vehicle()
//console.log('Public member, ', obj.publicMember)
//console.log('Private member, ', obj.myPrivateMember)
//console.log('Private member, ', obj.#privateMember)//it will not work

/*console.log('Calling Public member method, ')
obj.publicMethod()
console.log('Calling Private member method, ')
obj._privateMethod()

console.log('Calling Public static method, ')
Vehicle.publicMethod()
console.log('Calling Private static method, ')
Vehicle._privateMethod()*/

//console.log('Public static member, ', Vehicle.staticMember)
//console.log('Private static member, ', Vehicle.privateStaticMember)


let obj2 = new TwoWheeler()
console.log(obj2.getWheelCount())
obj2.publicMethod()


console.log('Everything is done!')