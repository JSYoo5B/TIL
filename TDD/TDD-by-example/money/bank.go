package money

type Bank struct {
	rateTable map[string]int
}

func (b *Bank) Reduce(source Expression, currency string) Money {
	return source.Reduce(b, currency)
}
func (b *Bank) AddRate(from, to string, rate int) {
	if from == to {
		// Skip same currency rate
		return
	}

	currencyName := from + to
	b.rateTable[currencyName] = rate
}
func (b *Bank) Rate(from, to string) int {
	if from == to {
		return 1
	}
	currencyName := from + to
	return b.rateTable[currencyName]
}

func NewBank() *Bank {
	return &Bank{
		rateTable: make(map[string]int),
	}
}
