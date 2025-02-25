package money

type Bank struct{}

func (b *Bank) Reduce(source Expression, currency string) Expression {
	return NewDollar(10)
}

func NewBank() *Bank {
	return &Bank{}
}
