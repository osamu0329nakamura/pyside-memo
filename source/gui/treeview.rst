QTreeView -- �c���[�r���[
#####################################


QTreeWidget
===============

�ȒP�ȃc���[�\���ł���΁AQTreeWidget ���g�p����Ƃ悢�B


TreeModel �̎���
=================

- root (model.index(0, 0, QModelIndex()))
  - child1 (model.index(0, 0, model.index(0, 0)))
  - child2 (model.index(1, 0, model.index(0, 0)))

�ȉ��̃��\�b�h����������B

- ``rowCount(index=QModelIndex())``
- ``columnCount(index=QModelIndex())``
- ``data(index, role)``
- ``index(row, column, parent=QModelIndex())``
- ``parent(index) : QModelIndex``

QModelIndex
-----------

QModelIndex �́A ``QAbstractItemModel.createIndex(row, column, data)`` �ō쐬����B

index.internalPointer() �܂��� index.internalId() �Ŋ֘A�t�����f�[�^���擾����B

data �� int �� bool ��^���āAinternalPointer() ���Ăяo���ƁA�N���b�V�����邽�ߒ��ӂ��K�v�B

rowCount �̎���
----------------

rowCount(index=QModelIndex()) -> 1 (�g�b�v���x���̗v�f��)


columnCount �̎���
------------------

columnCount(index=QModelIndex())

�c���[�̐[���Ɋ֌W�Ȃ��J���������Ȃ�Aindex �̒l�ɂ�炸�Œ�̐��l��Ԃ��Ƃ悢::

   def columnCount(index):
       return 2

index �̎���
------------

::

   def index(row, column, parent = QModelIndex()) -> QModelIndex

createIndex(row, column, data) ���g�p����B

parent.isValid() �� False �Ȃ�΁A�g�b�v���x���̗v�f

parent.isValid() �� True �Ȃ�΁A�g�b�v���x����艺�̗v�f�Ȃ̂ŁA

parent.internalPointer() �Őe�v�f�ɑΉ�����I�u�W�F�N�g���擾���āA
���̃I�u�W�F�N�ƁArow�Acolumn ����Ή�����q�v�f���擾����B

���̗v�f�� data �Ɏw�肵�āA createIndex(row, column, data) ���Ăяo���B

parent �̎���
--------------

::

   def parent(index) -> QModelIndex:

createIndex(row, column, data) ���g�p���ĕԂ��B

���ӁFindex.parent() ���Ăяo���Ă͂Ȃ�Ȃ��B�������[�v����B



