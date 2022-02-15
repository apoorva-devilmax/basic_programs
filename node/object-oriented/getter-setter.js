"use strict"


class ClassWithPrivateAccessor {
  #message

  get decoratedMessage()
  {
    return `✨ ${this.#message} ✨`
  }
  
  set decoratedMessage(msg) {
    this.#message = msg
  }

  constructor() {
    this.decoratedMessage = 'hello world'
    console.log(this.decoratedMessage)
  }

  static _privateStaticMethod() {
    return 42;
  }


}

new ClassWithPrivateAccessor();
// expected output: "✨hello worl​d✨"