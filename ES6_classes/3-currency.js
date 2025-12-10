export default class Currency {
  constructor(code, name) {
    // Verify code param is a string
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }

    // Verify name param is a string
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    this._code = code;
    this._name = name;
  }

  // ! Every setter must verify type for new input !
  // getting & setting for 'code' attr
  get code() {
    return this._code;
  }
  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }
  // getting & setting for 'name' attr
  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}
