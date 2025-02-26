package money

type Expression interface{}

type Sum struct {
	Augend Money
	Addend Money
}

func NewSum(augend, addend Money) *Sum {
	return &Sum{
		Augend: augend,
		Addend: addend,
	}
}
