package money

type Bank struct{}

func (b *Bank) Reduce(source Expression, currency string) Expression {
	sum := source.(*Sum)
	amount := sum.Augend.getAmount() + sum.Addend.getAmount()
	return newMoney(amount, currency)
}

func NewBank() *Bank {
	return &Bank{}
}
