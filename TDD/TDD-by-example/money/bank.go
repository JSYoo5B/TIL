package money

type Bank struct{}

func (b *Bank) Reduce(source Expression, currency string) Money {
	return source.Reduce(b, currency)
}
func (b *Bank) AddRate(from, to string, rate int) {
	// TODO: do something to register rate
}
func (b *Bank) Rate(from, to string) int {
	if from == "CHF" && to == "USD" {
		return 2
	} else {
		return 1
	}
}

func NewBank() *Bank {
	return &Bank{}
}
