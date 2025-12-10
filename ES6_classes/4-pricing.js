import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    // Verify amount is of the expected type
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    /* Verify currency is a Currency object;
    'code' and 'name' attr of Currency obj should be valid,
    as the class itself has getters & setters for verification*/
    if (!(currency instanceof Currency)) {
      throw new TypeError('currency must be an instance of the Currency class');
    }
    this._amount = amount;
    this._currency = currency;
  }

  // Using getters & setters to validate before updating values
  get amount() {
    return this._amount;
  }
  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }

  get currency() {
    return this._currency;
  }
  set currency(newCurrency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('currency must be an instance of the Currency class');
    }
    this._currency = newCurrency;
  }

  // Instance method
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static/Class method
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
