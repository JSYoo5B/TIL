package money

type Money interface {
	Times(multiplier int) Money
	Equals(other any) bool
	Currency() string
	getAmount() int
}

type money struct {
	amount   int
	currency string
}

func (m *money) Times(multiplier int) Money {
	return newMoney(m.amount*multiplier, m.currency)
}
func (m *money) Equals(other any) bool {
	otherMoney, ok := other.(Money)
	return ok &&
		m.amount == otherMoney.getAmount() &&
		m.currency == otherMoney.Currency()
}
func (m *money) Plus(other Money) Money {
	return newMoney(m.amount+other.getAmount(), m.currency)
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
