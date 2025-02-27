package money

type Expression interface {
	Reduce(to string) Money
}

type Sum struct {
	Augend Money
	Addend Money
}

func (s *Sum) Reduce(to string) Money {
	amount := s.Augend.getAmount() + s.Addend.getAmount()
	return newMoney(amount, to)
}

func NewSum(augend, addend Money) *Sum {
	return &Sum{
		Augend: augend,
		Addend: addend,
	}
}
