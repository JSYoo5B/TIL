package money

type Money interface {
	Times(multiplier int) Money
	Equals(other any) bool
}

type money struct {
	amount   int
	currency string
}

func (m *money) Currency() string {
	return m.currency
}
