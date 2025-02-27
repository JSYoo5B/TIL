package money

type Bank struct{}

func (b *Bank) Reduce(source Expression, currency string) Money {
	return source.Reduce(currency)
}

func NewBank() *Bank {
	return &Bank{}
}
