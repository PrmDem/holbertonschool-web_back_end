export default class Car {
  constructor(brand, motor, color) {
    // No verification of attr type since clone attr are all undefined
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() { return this._brand; }
  get motor() { return this._motor; }
  get color() { return this._color; }
  static get [Symbol.species]() { return this; }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
