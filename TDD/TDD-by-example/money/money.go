package money

type Money interface {
	Times(multiplier int) Expression
	Equals(other any) bool
	Currency() string
	getAmount() int

	Expression
}

type money struct {
	amount   int
	currency string
}

func (m *money) Times(multiplier int) Expression {
	return newMoney(m.amount*multiplier, m.currency)
}
func (m *money) Equals(other any) bool {
	otherMoney, ok := other.(Money)
	return ok &&
		m.amount == otherMoney.getAmount() &&
		m.currency == otherMoney.Currency()
}
func (m *money) Plus(addend Expression) Expression {
	return NewSum(m, addend)
}
func (m *money) Reduce(bank *Bank, to string) Money {
	rate := bank.Rate(m.currency, to)
	return newMoney(m.amount/rate, to)
}
func (m *money) Currency() string {
	return m.currency
}
func (m *money) getAmount() int {
	return m.amount
}

func newMoney(amount int, currency string) *money {
	return &money{
		amount:   amount,
		currency: currency,
	}
}
