# Beta notes: Piscine Deep Learning - 2 (Vision)

Page numbers are the printed ones (PDF page = printed page + 2).

## Issues

- **Ex02 / p. 7**: "A correct CNN should comfortably pass 0.85 test accuracy" vs the note "you may train on a subset, but your test accuracy must still be clearly above chance" → two different bars; an evaluator can't tell whether 0.6 on a subset passes or fails. (found by Claude, unconfirmed)
- **Ex02 / p. 7**: number of epochs, batch size and what "train loss" means (epoch mean or last batch) are not stated; only the example output shows 3 epochs → minor, but evaluators may disagree on whether the output format is right. (found by Claude, unconfirmed)
- **Ex03 / p. 8**: "Load your trained model (or retrain it)" → ex02 never asks to save weights, "Files to Submit" lists only `cnn.py` / `evaluate.py`, and it's not said whether `evaluate.py` may import the model class from `ex02/` or whether a weights file may be committed. (found by Claude, unconfirmed)
- **Ex03 / p. 8**: text asks to "Print the shape of the confusion matrix and the per-class accuracy", but the expected output also prints `Overall accuracy: 0.89` → text and expected output disagree. (found by Claude, unconfirmed)
- **Ex03 / p. 8**: only the *shape* of the confusion matrix is printed → `torch.Size([10, 10])` proves nothing about whether the counts are right; printing the matrix (or its sum = 10000) would let an evaluator check it. (found by Claude, unconfirmed)
- **Ex03 / p. 8**: "per-class accuracy" is not defined, and the matrix orientation (rows = true or predicted) isn't fixed → normalising by row (recall) or by column (precision) gives different numbers. The hint "(true label, predicted label) pairs" suggests rows = true, but it isn't explicit. (found by Claude, unconfirmed)
- **Ex04 / p. 9**: expected output says `Validation accuracy`, but no validation split is described (CIFAR-10 ships only train/test, and ex02/ex03 use "test accuracy") → unclear which set to evaluate on. (found by Claude, unconfirmed)
- **Ex04 / p. 9**: no hint that CIFAR-10 images (32×32) should be resized and normalised with ImageNet statistics for a pretrained resnet18 → training only the head on raw 32×32 images likely lands well below the 0.78 shown; needs checking. Evidence so far: at 32×32 resnet18's `layer4` output is 1×1 (checked with torch 2.15 / torchvision 0.29.2), and `ResNet18_Weights.DEFAULT.transforms()` resizes to 256, crops to 224 and uses ImageNet mean/std. (found by Claude, unconfirmed)
- **Ex04 / p. 9**: "a good accuracy" and "a small dataset (for example a subset of CIFAR-10)" have no numbers → no pass threshold and no subset size, so grading is subjective. (found by Claude, unconfirmed)
- **General Rules / p. 3 + Ex04**: "The datasets are downloaded through torchvision; download them once before your defense" → doesn't mention the pretrained ImageNet weights for ex04, which are also downloaded on first use and can fail offline during a defense. (found by Claude, unconfirmed)
- **General Rules / p. 3 vs Ex01 / p. 6**: matplotlib is allowed "only where a plot is explicitly requested", yet ex01 lists matplotlib as authorized without requesting any plot (and ex00's plot is an optional bonus, not "explicitly requested"). (found by Claude, unconfirmed)
- **General Rules / p. 4 vs Ex02–Ex04**: every program must seed with `torch.manual_seed(42)`, yet the outputs say "values will vary" → minor, but worth saying that values vary across machines/hardware, not between runs. (found by Claude, unconfirmed)

## Feedback form

(filled in during the review)
