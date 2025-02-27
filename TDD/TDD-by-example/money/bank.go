package money

type Bank struct{}

func (b *Bank) Reduce(source Expression, currency string) Money {
	if m, ok := source.(Money); ok {
		return m
	} else if sum, ok := source.(*Sum); ok {
		return sum.Reduce(currency)
	}
	return nil
}

func NewBank() *Bank {
	return &Bank{}
}
